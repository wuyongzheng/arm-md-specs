## A5.3 Host view of memory management

This section describes memory management from the Host's point of view.

## A5.3.1 Host IPA state

A Realm IPA has an associated Host IPA state (HIPAS).

The HIPAS values are shown in the following table.

| Name                | Description                                               |
|---------------------|-----------------------------------------------------------|
| HIPAS_ASSIGNED      | Protected IPA which is associated with a DATA Granule.    |
| HIPAS_ASSIGNED_NS   | Unprotected IPA which is associated with an NS Granule.   |
| HIPAS_UNASSIGNED    | Protected IPA which is not associated with any Granule.   |
| HIPAS_UNASSIGNED_NS | Unprotected IPA which is not associated with any Granule. |

HIPAS values are stored in a Realm Translation Table (RTT).

HIPAS transitions are caused by execution of RMI commands.

A mapping at a Protected IPA is valid if the HIPAS is ASSIGNED and the RIPAS is RAM.


The following table summarizes, for each combination of RIPAS and HIPAS for a Protected IPA:

- the translation table entry attributes, and
- the behavior which results from Realm access to that IPA.

Each TTD.X column refers to the value of the corresponding 'X' field in the architecturally-defined Stage 2 translation table descriptor which is written by the RMM.

| RIPAS     | HIPAS      | TTD.ADDR   | TTD.NS   |   TTD.VALID | Data access                | Instruction fetch                 |
|-----------|------------|------------|----------|-------------|----------------------------|-----------------------------------|
| EMPTY     | UNASSIGNED |            |          |           0 | SEA to Realm               | SEA to Realm                      |
| EMPTY     | ASSIGNED   | DATA       |          |           0 | SEA to Realm               | SEA to Realm                      |
| RAM       | UNASSIGNED |            |          |           0 | REC exit due to Data Abort | REC exit due to Instruction Abort |
| RAM       | ASSIGNED   | DATA       | 0        |           1 | Data access                | Instruction fetch                 |
| DESTROYED | UNASSIGNED |            |          |           0 | REC exit due to Data Abort | REC exit due to Instruction Abort |
| DESTROYED | ASSIGNED   | DATA       |          |           0 | REC exit due to Data Abort | REC exit due to Instruction Abort |

## See also:

- A5.5 Realm Translation Table

## A5.3.2 Changes to HIPAS while Realm state is REALM\_NEW

This section describes how the HIPAS of a Protected IPA can change while the Realm state is REALM\_NEW.

- The following diagram summarizes HIPAS changes at a Protected IPA which can occur when the Realm state is REALM\_NEW.

<!-- image -->

## See also:

- B4.3.1 RMI\_DATA\_CREATE command
- B4.3.2 RMI\_DATA\_CREATE\_UNKNOWN command
- B4.3.3 RMI\_DATA\_DESTROY command
- B4.3.16 RMI\_RTT\_DESTROY command

## A5.3.3 Changes to HIPAS while Realm state is REALM\_ACTIVE

This section describes how the HIPAS of a Protected IPA can change while the Realm state is REALM\_ACTIVE.

The following diagram summarizes HIPAS changes at a Protected IPA which can occur when the Realm state is REALM\_ACTIVE.

<!-- image -->

## See also:

- B4.3.2 RMI\_DATA\_CREATE\_UNKNOWN command
- B4.3.3 RMI\_DATA\_DESTROY command
- B4.3.16 RMI\_RTT\_DESTROY command

## A5.3.4 Summary of changes to HIPAS and RIPAS of a Protected IPA

The following diagram summarizes HIPAS and RIPAS changes at a Protected IPA which can occur when the Realm state is NEW.

<!-- image -->

The following diagram summarizes HIPAS and RIPAS changes at a Protected IPA which can occur when the Realm state is REALM\_ACTIVE.

<!-- image -->

<!-- image -->

## See also:

- B4.3.1 RMI\_DATA\_CREATE command
- B4.3.2 RMI\_DATA\_CREATE\_UNKNOWN command
- B4.3.3 RMI\_DATA\_DESTROY command
- B4.3.16 RMI\_RTT\_DESTROY command
- B4.3.18 RMI\_RTT\_INIT\_RIPAS command
- B4.3.21 RMI\_RTT\_SET\_RIPAS command

## A5.3.5 Dependency of RMI command execution on RIPAS and HIPAS values

The following table summarizes dependencies on RMI command execution on the current Protected IPA.

| Command                 | Dependency on RIPAS                                       | Dependency on HIPAS                | New RIPAS             | New HIPAS   |
|-------------------------|-----------------------------------------------------------|------------------------------------|-----------------------|-------------|
| RMI_DATA_CREATE         | None                                                      | HIPAS is UNASSIGNED                | RAM                   | ASSIGNED    |
| RMI_DATA_CREATE_UNKNOWN | None                                                      | HIPAS is UNASSIGNED                | Unchanged             | ASSIGNED    |
| RMI_DATA_DESTROY        | If RIPAS is EMPTY                                         | HIPAS is ASSIGNED                  | Unchanged             | UNASSIGNED  |
| RMI_DATA_DESTROY        | If RIPAS isRAM                                            | HIPAS is ASSIGNED                  | DESTROYED             | UNASSIGNED  |
| RMI_RTT_CREATE          | None                                                      | None                               | Unchanged             | Unchanged   |
| RMI_RTT_DESTROY         | None                                                      | HIPAS of all entries is UNASSIGNED | DESTROYED             | Unchanged   |
| RMI_RTT_FOLD            | RIPAS of all entries is identical                         | HIPAS of all entries is identical  | Unchanged             | Unchanged   |
| RMI_RTT_INIT_RIPAS      | None                                                      | HIPAS is UNASSIGNED                | RAM                   | Unchanged   |
| RMI_RTT_SET_RIPAS       | Optionally, Realm may specify that RIPAS is not DESTROYED | None                               | As specified by Realm | Unchanged   |


Successful execution of RMI\_DATA\_CREATE\_UNKNOWN does not depend on the RIPAS value of the target IPA.



Successful execution of RMI\_DATA\_DESTROY does not depend on the RIPAS value of the target IPA.

Successful execution of RMI\_RTT\_DESTROY does not depend on the RIPAS values of entries in the target RTT.

Successful execution of RMI\_RTT\_FOLD does depend on the RIPAS values of entries in the target RTT. See also:

- B4.3.1 RMI\_DATA\_CREATE command
- B4.3.2 RMI\_DATA\_CREATE\_UNKNOWN command
- B4.3.3 RMI\_DATA\_DESTROY command
- B4.3.15 RMI\_RTT\_CREATE command
- B4.3.16 RMI\_RTT\_DESTROY command
- B4.3.17 RMI\_RTT\_FOLD command
- B4.3.18 RMI\_RTT\_INIT\_RIPAS command
- B4.3.21 RMI\_RTT\_SET\_RIPAS command

## A5.3.6 Changes to HIPAS of an Unprotected IPA

The following diagram summarises HIPAS transitions for an Unprotected IPA.

<!-- image -->

See also:

Chapter A5. Realm memory management A5.3. Host view of memory management

- A5.4 RIPAS change
- A5.5 Realm Translation Table
- B4.3.1 RMI\_DATA\_CREATE command
- B4.3.2 RMI\_DATA\_CREATE\_UNKNOWN command
- B4.3.3 RMI\_DATA\_DESTROY command
- B4.3.16 RMI\_RTT\_DESTROY command
- B4.3.18 RMI\_RTT\_INIT\_RIPAS command
- B4.3.21 RMI\_RTT\_SET\_RIPAS command
- B5.3.6 RSI\_IPA\_STATE\_SET command