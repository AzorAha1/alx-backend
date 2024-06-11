import { createClient } from 'redis';

const client = createClient({
    url: 'redis://localhost:6379'
})

// catch error
client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
})
// when connect connect
client.on('connect', () => {
    console.log('Redis client connected to the server')
})
