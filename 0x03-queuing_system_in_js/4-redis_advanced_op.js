import { createClient, print } from 'redis';

const client = createClient({
    url: 'redis://localhost:6379'
});

// Catch error
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

// Successful connection
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Using hset to store hash values
client.hset('HolbertonSchools', 'Portland', 50, print);
client.hset('HolbertonSchools', 'Seattle', 80, print);
client.hset('HolbertonSchools', 'New York', 20, print);
client.hset('HolbertonSchools', 'Bogota', 20, print);
client.hset('HolbertonSchools', 'Cali', 40, print);
client.hset('HolbertonSchools', 'Paris', 2, print);

// Using hgetall to display all hash values
client.hgetall('HolbertonSchools', (error, hashsets) => {
    if (error) {
        console.log(error);
    } else {
        console.log(hashsets);
    }
});
