import { createClient, print } from 'redis';
import { promisify } from 'util'
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

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}
const getAsync = promisify(client.get).bind(client)
async function displaySchoolValue(schoolName) {
    try {
        const response = await getAsync(schoolName)
        console.log(response)
    } catch (error) {
        console.log(`this is the error message: ${error}`)
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');