## A1.7 Reliability, Availability, and Serviceability

## A1.7.1 Introduction

ILMHPD

RAS are three aspects of the dependability of a system:

- Reliability, that is, the continuity of correct service.

- Availability, that is, the readiness for correct service.

- Serviceability, that is, the ability to undergo modifications and repairs.

IHWHJM

RAS techniques reduce unplanned outages because:

- Transient errors can be detected and corrected before they cause application or system failure.

- Failing components can be identified and replaced.

- Failure can be predicted ahead-of-time to allow replacement during planned maintenance.

## A1.7.2 Faults, errors, and failures

RNVNNC

Correct service is delivered when the service implements the system function.

IQWSVK Correct service might include:

- Producing correct results.
- Producing results within the time allotted to the task.
- Not divulging secret or secure information.

For the purpose of describing the RAS Extension and RAS System Architecture, deviation from correct service is defined using the following terms:

- Afailure is the event of deviation from correct service. This includes data corruption, data loss, and service loss.
- An error is the deviation from correct service. An incorrect value that has an error is corrupt.
- Afault is the cause of the error.

RJNBDX Errors that are present but not detected are latent errors or undetected errors.

ITNQPK In a system with no error detection, all errors are latent errors and are silently propagated by components until they are either masked or cause failure.

IGRYKV The severity of a failure can range from minor to catastrophic:

- The harmful consequences of a minor failure are of a similar cost to the benefits provided by correct service delivery.
- The harmful consequences of a catastrophic failure are orders of magnitude, or even incommensurably, higher than the benefit provided by correct service delivery.
- There are many sources of faults in a system, including both software and hardware faults:
- Hardware faults originate in, or affect, hardware.
- Software faults affect software, that is programs or data.

The RAS Extension and RAS System Architecture primarily address errors produced from hardware faults. These fall into two main areas:

- Transient faults.
- Non-transient or persistent faults .

## A1.7.3 General taxonomy of errors

## A1.7.3.1 Error detection

RFHXWP

When a component accesses memory or other state, an error might be detected in that memory or state.

IWKPVR

The error might be corrected or deferred by the component, or signaled to another component as either a Deferred error or a Detected error.

RKRTSC

INMGPQ

## A1.7.3.2 Error propagation

| R LRZDN   | Atransaction occurs when a producer of the transaction passes a value or other signal to a consumer of the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I VYCCX   | Transactions are part of the service provided by the producer for the consumer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| I RHGDL   | In many protocols and service interface definitions, a high-level transaction consists of a sequence of operations, for instance between a Requester and a Completer . For the purposes of this manual, the most basic form of a unidirectional transfer between a producer and consumer is considered as a transaction. That is, each one of the sequence of operations is considered a separate transaction. For some operations, such as a request, the Requester is producer and the Completer is the consumer. For other operations, such as a response, the Completer is producer and the Requester is the consumer. |
| R SKZZG   | An error is propagated by the producer of a transaction when the service interface is incorrect because of the error. The error is propagated to the consumer.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| R CHCCV   | An error is propagated by deviations from correct service, including when any of the following occurs that would not have been permitted to occur had the fault not been activated:                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| R YFBRV   | The service interface for a transaction might include means to signal that the transaction is propagating either of the following: • ADetected error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| R BHWVX   | An error is silently propagated by the producer of a transaction if the consumer of the transaction cannot detect the error and consumes an undetected error because of the transaction. This might be because of one of the following: • The error is present on the transaction, but was not detected by the producer. The error is silently propagated by the producer. • The error is present on the transaction, but was not signaled to the consumer as an error. For example, a corrupt value was passed in the transaction with no indication that it was corrupt. The error is silently propagated by the         |
| R FPBYS   | Alatent, possibly detectable, error is silently propagated by the consumer of an otherwise correct transaction if the transaction causes the error to become undetectable. Example A1-2 A partial write to a protection granule removes poison, leaving the unchanged portion of the location corrupt. To implement a partial write, the consumer logically reads the current value of the location, modifies the value, and then writes the modified value back. These are internal transactions in the consumer that silently propagate the                                                                              |
|           | error. In this example there was no error at the producer nor on the transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| I QXRLB   | Errors might be propagated by components in a system until one of the following occurs: • They are masked and do not affect the outcome of the system. The error might be masked because a corrupt value is discarded or overwritten, or the error is detected and removed. • They affect the service interface of the system and possibly cause failure. If the error has been silently propagated                                                                                                                                                                                                                        |

- -The rate of such failures, measured as the number of failures per billion device-hours of operation, is called the Silent Data Corruption Failure-in-Time rate, SDC FIT rate.

Alternatively, the error might have been detected, causing the system to invoke error handling and recovery. For more information, see Arm ® Reliability, Availability, and Serviceability (RAS) System Architecture, for A-profile architecture (ARM IHI 0100).

## A1.7.3.3 Infected and poisoned

| R KNHWB   | The state of a component becomes infected when the component consumes an Uncorrected error that updates the state.                                                                                                                                                                                                                                                                                                                                         |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R TZBSW   | Avalue is poisoned in the state of a component if it is marked as being in error, such that a subsequent access of the state will detect the value is so marked and is treated as a Detected error.                                                                                                                                                                                                                                                        |
| I YBMFK   | Poison is used to defer an error.                                                                                                                                                                                                                                                                                                                                                                                                                          |
|           | A1.7.3.4 Containable and uncontainable                                                                                                                                                                                                                                                                                                                                                                                                                     |
| R DXQRD   | An undetected error is uncontained at the component that failed to detect it.                                                                                                                                                                                                                                                                                                                                                                              |
| R RJYRQ   | Asilently propagated error is uncontained at the component that silently propagated it.                                                                                                                                                                                                                                                                                                                                                                    |
| R GJQNR   | ADetected Uncorrected error is uncontainable at the component if it might be uncontained at the component. A Detected Uncorrected error is containable at the component if it is not uncontainable at the component. If the component cannot determine whether a Detected Uncorrected error is uncontainable at the component or containable at the component, then the component treats the Detected Uncorrected error as uncontainable at the component. |
| I MRDMR   | An error that is uncontainable at the component might be containable at the system level.                                                                                                                                                                                                                                                                                                                                                                  |
| I NWZGB   | Reporting an error as containable allows software to contain the error. This does not mean that hardware has contained the error.                                                                                                                                                                                                                                                                                                                          |

## Chapter A2 A-profile Architecture Extensions

This chapter introduces the Arm A-profile architecture extensions. It contains the following sections:

- About the A-profile architecture extensions.
- Armv8-A architecture extensions.
- Armv9-A architecture extensions.