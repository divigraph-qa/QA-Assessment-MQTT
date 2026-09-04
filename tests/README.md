# QA test assignment

### *** Keep in mind that the System Under Test is the Simulated Service (publisher) *** ###
Create a test framework inside the `tests/` folder. Choose a language and test framework that you can explain and maintain, and keep the test setup and instructions in that folder.<br>
The test should connect to `localhost:1883`, subscribe to the topic configured in `publisher/.env`, and collect several messages before making assertions.

### Write automated tests that verifies the following:

1. The topic structure and naming is correct
2. Each message has `status` set to `ONLINE`.
3. Each message has `deviceId` set to `DEVICE001`.
4. Messages arrive approximately every 5 seconds.
5. Each `temperature` value is between the configured lower and upper bounds, inclusive. The defaults are `20` and `30`; the test should make these bounds configurable so it remains valid when `TEMP_LOWER_BOUND` or `TEMP_UPPER_BOUND` changes.
6. The publisher's `timestamp` is no more than 10 minutes away from the test machine's current UTC time. Parse the ISO 8601 timestamp and compare it with the current UTC time, not with a local clock string.
7. You may add more tests as you see fit, as long as the above 6 test cases are covered at a minimum.

The test should fail with a useful message when a message is missing, malformed, on the wrong topic, outside the expected interval, outside the temperature bounds, has the wrong device status or ID, or has a timestamp drift greater than 10 minutes.



# Documentation

### *** Add the documenation for setting up and running your tests here ***