import { createClient, print } from 'redis';

const subscriberclient = createClient({
    url: 'redis://localhost:6379'
});

// Catch error
subscriberclient.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

// Successful connection
subscriberclient.on('connect', () => {
    console.log('Redis client connected to the server');
    subscriberclient.subscribe('holberton school channel', (err, content) => {
        if (err) {
            console.log(err)
        } else {
            console.log(content)
        }
    })
});
subscriberclient.on('message', (channel, message) => {
    console.log(`Received message from ${channel}: ${message}`);
    if (message === 'KILL_SERVER') {
        subscriberclient.unsubscribe('holberton school channel', () => {
            console.log(`Unsubscribed from ${channel}`);
            subscriberclient.quit();
        });
    }
});
