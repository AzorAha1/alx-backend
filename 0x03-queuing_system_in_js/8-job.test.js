const { expect } = require('chai');
const { describe, it, before, after, afterEach } = require('mocha');
const kue = require('kue');
const createPushNotificationsJobs = require('./8-job.js');

let queue;

describe('createPushNotificationsJobs test', () => {
    before(() => {
        queue = kue.createQueue();
        kue.Job.rangeByState('inactive', 0, 500, (error, jobs) => {
            if (error) throw error;
            jobs.forEach(job => job.remove());
        });
        queue.testMode.enter();
    });

    afterEach(() => {
        queue.testMode.clear();
    });

    after(() => {
        queue.testMode.exit();
    });

    it('should throw an error if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs(1, queue)).to.throw('Jobs is not an array');
    });

    it('should create jobs and check if they have valid job data', () => {
        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '4153518781',
                message: 'This is the code 4562 to verify your account'
            },
            {
                phoneNumber: '4153518743',
                message: 'This is the code 4321 to verify your account'
            }
        ];
        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs.length).to.equal(3);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code');
    });
});
