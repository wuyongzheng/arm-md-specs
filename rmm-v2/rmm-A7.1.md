## A7.1 Realm measurements

This section describes how Realm measurement values are calculated.

DSJWWS A Realm measurement value is an incremental hash.

DYKDBY A Realm Hash Algorithm (RHA) is an algorithm which is used to extend a Realm measurement value.

INRKWB The RHA used by a Realm is selected via the hash\_algo attribute.

See also:

- A2.2.3 Realm attributes
- A3.2 Realm hash algorithm
- A7.2.3.1.5 Realm Initial Measurement claim
- A7.2.3.1.6 Realm Extensible Measurements claim

## A7.1.1 Realm Initial Measurement

This section describes how the Realm Initial Measurement (RIM) is calculated.

- IXKSBZ The initial RIM value for a Realm is zero.
- INCNDK A RIM is extended by applying the RHA to the inputs of RMM operations which are executed during Realm construction.

INQQTF The following operations cause a RIM to be extended:

- Creation of a DATA Granule during Realm construction
- Creation of a runnable REC
- Changes to RIPAS of Protected IPA during Realm construction
- RVMPZG On execution of an operation which requires extension of a RIM, the RMM first constructs a measurement descriptor structure. The measurement descriptor contents include the current RIM value. The new RIM value is computed by applying the RHA to the measurement descriptor.

<!-- formula-not-decoded -->

- IFQHFC A RIM is immutable while the state of the Realm is REALM\_ACTIVE. This implies that a RIM reflects the configuration and contents of the Realm at the moment when it transitioned from the REALM\_NEW to the REALM\_ACTIVE state.

IDQGPT A RIM depends upon the order of the RMM operations which are executed during Realm construction.

SVZNCW The order in which RMM operations are executed during Realm construction must be agreed between the Realm owner (or a delegate of the Realm owner which will receive and validate the RIM) and the Host which executes the RMMcommands. This ensures that a correctly-constructed Realm will have the expected measurement.

ILTWBL The value of a RIM can be read using the RSI\_MEASUREMENT\_READ command.

See also:

- B4.5.46.4 RMI\_REALM\_CREATE initialization of RIM
- B4.5.49.4 RMI\_REC\_CREATE extension of RIM
- B4.5.66.4 RMI\_RTT\_DATA\_MAP\_INIT extension of RIM
- B5.4.9 RSI\_MEASUREMENT\_READ command

## A7.1.2 Realm Extensible Measurement

This section describes the behavior of a Realm Extensible Measurement (REM).

## Chapter A7. Realm measurement and attestation

A7.1. Realm measurements

IQJDWM A REM is extended using the RSI\_MEASUREMENT\_EXTEND command.

- ICTMBT The value of a REM can be read using the RSI\_MEASUREMENT\_READ command.

IMDQRP The initial value of a REM is zero.

See also:

- B5.4.8 RSI\_MEASUREMENT\_EXTEND command
- B5.4.9 RSI\_MEASUREMENT\_READ command

<!-- image -->