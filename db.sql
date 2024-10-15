CREATE DATABASE Hospital;
USE Hospital;

DROP TABLE IF EXISTS patients;

CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    phoneNumber VARCHAR(255) NOT NULL,
    secondaryPhoneNumber VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    admissionDate DATETIME NOT NULL,
    dischargeDate DATETIME NOT NULL,
    contactDate DATE NOT NULL,
    admissionReason VARCHAR(1024) NOT NULL,
    proceduresPerformed VARCHAR(1024) NOT NULL,
    diagnosis VARCHAR(1024) NOT NULL,
    medicationsGiven VARCHAR(1024) NOT NULL,
    followupInstructions VARCHAR(1024) NOT NULL,
    authCode VARCHAR(255) NOT NULL,
    needsFollowUp BOOLEAN NOT NULL
);

-- phone number
-- patient name
-- contact schedule
-- 

-- I need to create the database using this script
-- Then I need to do the following
-- We should be able to handle requests to the backend endpoint which adds/updates/deletes patients to the database
-- Every 15 minutes, the backend
