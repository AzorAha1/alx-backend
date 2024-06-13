const { createClient } = require('redis');
const { promisify } = require('util');
const express = require('express');
const kue = require('kue');
const queue = kue.createQueue();
const client = createClient({
    url: 'redis://localhost:6379'
});
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);
const app = express();
const port = 1245;

let reservationEnabled = true;

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', async () => {
    await reserveSeat(50);
    console.log('Redis client connected to the server');
});

async function reserveSeat(number) {
    await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
    const currentSeats = await getAsync('available_seats');
    return parseInt(currentSeats, 10) || 0;
}

app.get('/available_seats', async (req, res) => {
    const seats = await getCurrentAvailableSeats();
    return res.json({ numberOfAvailableSeats: seats });
});

app.get('/reserve_seat', async (req, res) => {
    if (!reservationEnabled) {
        return res.json({ status: 'Reservations are blocked' });
    }

    const job = queue.create('reserve_seat').save((err) => {
        if (!err) {
            return res.json({ status: 'Reservation in process' });
        } else {
            return res.json({ status: 'Reservation failed' });
        }
    });

    job.on('complete', (result) => {
        console.log(`Seat reservation job ${job.id} completed`);
    }).on('failed', (error) => {
        console.log(`Seat reservation job ${job.id} failed: ${error}`);
    });
});
// Add the route GET /process that:

//     Returns { "status": "Queue processing" } just after:
//     Process the queue reserve_seat (async):
//         Decrease the number of seat available by using getCurrentAvailableSeats and reserveSeat
//         If the new number of available seats is equal to 0, set reservationEnabled to false
//         If the new number of available seats is more or equal than 0, the job is successful
//         Otherwise, fail the job with an Error with the message Not enough seats available
app.get('/process', async (req, res) => {
    res.json({ 'status': 'Queue processing' }); // Send the initial response

    queue.process('reserve_seat', async (job, done) => {
        try {
            let currentSeats = await getCurrentAvailableSeats();

            if (currentSeats >= 0) {
                await reserveSeat(currentSeats - 1);
                currentSeats--;

                if (currentSeats === 0) {
                    reservationEnabled = false;
                }

                console.log(`Seat reservation job ${job.id} completed`);
                done(); // Mark the job as done
            } else {
                console.log(`Seat reservation job ${job.id} failed: Not enough seats available`);
                done(new Error('Not enough seats available')); // Fail the job with an error
            }
        } catch (error) {
            console.error(`Seat reservation job ${job.id} failed: ${error.message}`);
            done(error); 
        }
    });
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
