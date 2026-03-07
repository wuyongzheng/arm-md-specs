## A7.1 Realm measurements

This section describes how Realm measurement values are calculated.

A Realm measurement value is a rolling hash.

A Realm Hash Algorithm (RHA) is an algorithm which is used to extend a Realm measurement value.

The RHA used by a Realm is selected via the hash\_algo attribute.

See also:

- [A2.1.3 Realm attributes](rmm-A2.1.md#a213-realm-attributes)
- [A3.1.1 Realm hash algorithm](rmm-A3.md#a311-realm-hash-algorithm)
- [A7.2.3.1.4 Realm Initial Measurement claim](rmm-A7.2.md#a72314-realm-initial-measurement-claim)
- [A7.2.3.1.5 Realm Extensible Measurements claim](rmm-A7.2.md#a72315-realm-extensible-measurements-claim)

## A7.1.1 Realm Initial Measurement

This section describes how the Realm Initial Measurement (RIM) is calculated.

- The initial RIM value for a Realm is calculated from a subset of the Realm parameters.
- A RIM is extended by applying the RHA to the inputs of RMM operations which are executed during Realm construction.

The following operations cause a RIM to be extended:

- Creation of a DATA Granule during Realm construction
- Creation of a runnable REC
- Changes to RIPAS of Protected IPA during Realm construction
- On execution of an operation which requires extension of a RIM, the RMM first constructs a measurement descriptor structure. The measurement descriptor contents include the current RIM value. The new RIM value is computed by applying the RHA to the measurement descriptor.

<!-- formula-not-decoded -->

- A RIM is immutable while the state of the Realm is REALM\_ACTIVE. This implies that a RIM reflects the configuration and contents of the Realm at the moment when it transitioned from the REALM\_NEW to the REALM\_ACTIVE state.

A RIM depends upon the order of the RMM operations which are executed during Realm construction.

The order in which RMM operations are executed during Realm construction must be agreed between the Realm owner (or a delegate of the Realm owner which will receive and validate the RIM) and the Host which executes the RMMcommands. This ensures that a correctly-constructed Realm will have the expected measurement.

The value of a RIM can be read using the RSI\_MEASUREMENT\_READ command.

See also:

- [B4.3.1.4 RMI\_DATA\_CREATE extension of RIM](rmm-B4.3.1.md#b4314-rmi_data_create-extension-of-rim)
- [B4.3.9.4 RMI\_REALM\_CREATE initialization of RIM](rmm-B4.3.9.md#b4394-rmi_realm_create-initialization-of-rim)
- [B4.3.12.4 RMI\_REC\_CREATE extension of RIM](rmm-B4.3.12.md#b43124-rmi_rec_create-extension-of-rim)
- [B4.3.18.4 RMI\_RTT\_INIT\_RIPAS extension of RIM](rmm-B4.3.18.md#b43184-rmi_rtt_init_ripas-extension-of-rim)
- [B5.3.8 RSI\_MEASUREMENT\_READ command](rmm-B5.3.8.md)

## A7.1.2 Realm Extensible Measurement

This section describes the behavior of a Realm Extensible Measurement (REM).

- A REM is extended using the RSI\_MEASUREMENT\_EXTEND command.
- The value of a REM can be read using the RSI\_MEASUREMENT\_READ command.
- The initial value of a REM is zero.

See also:

- [B5.3.7 RSI\_MEASUREMENT\_EXTEND command](rmm-B5.3.7.md)
- [B5.3.8 RSI\_MEASUREMENT\_READ command](rmm-B5.3.8.md)