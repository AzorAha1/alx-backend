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

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, print);
}
function displaySchoolValue(schoolName) {
    client.get(schoolName, (error, response) => {
        if (error) {
            console.log(error);
        } else {
            console.log(response);
        }
    });
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
