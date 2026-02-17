IZPNZT The Realm can query the RIPAS of an IPA range by executing RSI\_IPA\_STATE\_GET.

See also:

- A5.5 Realm Translation Table
- B5.3.5 RSI\_IPA\_STATE\_GET command

## A5.2.3 Realm access to a Protected IPA

- RJVQQR Realm data access to a Protected IPA whose RIPAS is EMPTY causes a Synchronous External Abort taken to the Realm.
- RMKLSD Realm instruction fetch from a Protected IPA whose RIPAS is EMPTY causes a Synchronous External Abort taken to the Realm.
- RQSQLF Realm data access to a Protected IPA whose RIPAS is RAM does not cause a Synchronous External Abort taken to the Realm.
- IPGHBT Realm data access to a Protected IPA can cause an REC exit due to Data Abort.
- RFCJCP Realm instruction fetch from a Protected IPA whose RIPAS is RAM does not cause a Synchronous External Abort taken to the Realm.
- IXHKQY Realm instruction fetch from a Protected IPA whose RIPAS is RAM can cause a REC exit due to Instruction Abort.
- RCLVKF Realm data access to a Protected IPA whose RIPAS is DESTROYED causes a REC exit due to Data Abort.
- RMZYQT Realm instruction fetch from a Protected IPA whose RIPAS is DESTROYED causes a REC exit due to Instruction Abort.

See also:

- A4.3.4.2 REC exit due to Instruction Abort
- A4.3.4.3 REC exit due to Data Abort
- A5.2.7 Synchronous External Aborts

## A5.2.4 Changes to RIPAS while Realm state is REALM\_NEW

This section describes how the RIPAS of a Protected IPA can change while the Realm state is REALM\_NEW.

- IBSBHN For a Realm in the REALM\_NEW state, the RIPAS of a Protected IPA can change to RAM due to Host execution of RMI\_DATA\_CREATE or RMI\_RTT\_INIT\_RIPAS.
- IBSGSW For a Realm in the REALM\_NEW state, changing the RIPAS of a Protected IPA to RAM causes the RIM to be updated.
- IYCPNY For a Realm in the REALM\_NEW state, the RIPAS of a Protected IPA can change to DESTROYED due to Host execution of RMI\_DATA\_DESTROY or RMI\_RTT\_DESTROY.
- IYXLCP For a Realm in the REALM\_NEW state, changing the RIPAS of a Protected IPA to DESTROYED does not cause the RIM to be updated.

See also:

- A5.4 RIPAS change
- A7.1.1 Realm Initial Measurement
- B4.3.3 RMI\_DATA\_DESTROY command
- B4.3.16 RMI\_RTT\_DESTROY command
- B4.3.18 RMI\_RTT\_INIT\_RIPAS command

## A5.2.5 Changes to RIPAS while Realm state is REALM\_ACTIVE

This section describes how the RIPAS of a Protected IPA can change while the Realm state is REALM\_ACTIVE.

- INZXPG A Realm in the REALM\_ACTIVE state can request the RIPAS of a region of Protected IPA space to be changed to either EMPTY or RAM.
- IRXHXF ARealm in the REALM\_ACTIVE state cannot request the RIPAS of a region of Protected IPA space to be changed to DESTROYED.
- IFRJJH For a Realm in the REALM\_ACTIVE state, the RIPAS of a Protected IPA can change to EMPTY only in response to Realm execution of RSI\_IPA\_STATE\_SET.
- XHQLVY The fact that the Host cannot change the RIPAS of a Protected IPA to EMPTY without the Realm having consented to this change prevents the Host from injecting an SEA at a Protected IPA which has been configured to have a RIPAS of RAM, which could potentially trigger unexpected behavior in the Realm.
- IHNFYR For a Realm in the REALM\_ACTIVE state, the RIPAS of a Protected IPA can change to RAM only in response to Realm execution of RSI\_IPA\_STATE\_SET.
- IVVFMX On execution of RSI\_IPA\_STATE\_SET, a Realm can optionally specify that the RIPAS change should only succeed if the current RIPAS is not DESTROYED.
- XVXHBV An expected pattern for Realm creation is as follows:
1. Host populates an 'initial image' range of Realm IPA space with measured content:

Host executes RMI\_DATA\_CREATE, establishing a mapping to physical memory, changing RIPAS to RAM and updating the RIM.

2. Host informs the Realm of the range of IPA space which should be considered by the Realm as DRAM. This is a superset of the IPA range populated in step 1. For unpopulated parts of this IPA range, the RIPAS is EMPTY.
3. Realm executes RSI\_IPA\_STATE\_SET(ripas=RAM) for the DRAM IPA range described to it in step 2. Following this command, the desired state is:
- a. For the initial image IPA range, the contents match those described by the RIM.
- b. For the entire DRAM IPA range, RIPAS is RAM.

If at step 2, the Host were to execute RMI\_DATA\_DESTROY on a page within the initial image IPA range, its RIPAS would change to DESTROYED. The Host could then execute RMI\_DATA\_CREATE\_UNKNOWN, with the result that contents of the initial image IPA range no longer match those described by the RIM.

By specifying at step 3 that the RIPAS change should only succeed if the current RIPAS is not DESTROYED, the Realm is able to prevent loss of integrity within the initial image IPA range.

- IKZVDC For a Realm in the REALM\_ACTIVE state, the RIPAS of a Protected IPA can change to DESTROYED due to Host execution of RMI\_DATA\_DESTROY or RMI\_RTT\_DESTROY.
- XJJPHJ The result of changing the RIPAS of a Protected IPA to DESTROYED is that subsequent Realm accesses to that address do not make forward progress. This is consistent with the principle that the RMM does not provide an availability guarantee to a Realm.

INMMSG The following diagram summarizes RIPAS changes which can occur when the Realm state is REALM\_ACTIVE.

<!-- image -->

## See also:

- A5.4 RIPAS change
- B4.3.1 RMI\_DATA\_CREATE command
- B4.3.2 RMI\_DATA\_CREATE\_UNKNOWN command
- B4.3.3 RMI\_DATA\_DESTROY command
- B4.3.16 RMI\_RTT\_DESTROY command
- B4.3.18 RMI\_RTT\_INIT\_RIPAS command
- B5.3.6 RSI\_IPA\_STATE\_SET command

## A5.2.6 Realm access to an Unprotected IPA

- IKQJML An access by a Realm to an Unprotected IPA can result in a Granule Protection Fault (GPF).

The RMM does not ensure that the GPT entry of a Granule mapped at an Unprotected IPA permits access via Non-secure PAS.

SZZBQF Realm software must be able to handle taking a GPF during access to an Unprotected IPA.

- IWCVBZ Realm data access to an Unprotected IPA can cause a REC exit due to Data Abort.

IRNDTJ On taking a REC exit due to Data Abort at an Unprotected IPA, the Host can inject a Synchronous External Abort to the Realm.

XMGBDH The Host can inject an SEA in response to an unexpected Realm data access to an Unprotected IPA.

IFVYCM Realm data access to an Unprotected IPA which caused ESR\_EL2.ISS.ISV to be set to '1' can be emulated by the Host.

- RXLSKP Realm instruction fetch from an Unprotected IPA causes a Synchronous External Abort taken to the Realm.

## See also:

- A4.2.3 REC entry following REC exit due to Data Abort
- A4.3.4.3 REC exit due to Data Abort
- A4.4 Emulated Data Aborts
- A5.2.7 Synchronous External Aborts

## A5.2.7 Synchronous External Aborts

RVKNJW When a Synchronous External Abort is taken to a Realm, ESR\_EL1.EA == '1' .

## A5.2.8 Realm access outside IPA space

- RGYVZQ If stage 1 translation is enabled, Realm access to an IPA which is greater than the IPA space of the Realm causes a stage 1 Address Size Fault taken to the Realm, with the fault status code indicating the level at which the fault occurred.
- RLSJJR If stage 1 translation is disabled, Realm access to an IPA which is greater than the IPA space of the Realm causes a stage 1 level 0 Address Size Fault taken to the Realm.

## A5.2.9 Summary of Realm IPA space properties

ITPGKW The following table summarizes the properties of Realm IPA space.

| Realm IPA                  | Data access causes abort to Realm?                       | Data access causes REC exit due to Data Abort?   | Instruction fetch causes abort to Realm?   | Instruction fetch causes REC exit due to Instruction Abort?   |
|----------------------------|----------------------------------------------------------|--------------------------------------------------|--------------------------------------------|---------------------------------------------------------------|
| Protected, RIPAS=EMPTY     | Always (SEA)                                             | Never                                            | Always (SEA)                               | Never                                                         |
| Protected, RIPAS=RAM       | Never                                                    | When HIPAS=UNASSIGNED                            | Never                                      | When HIPAS=UNASSIGNED                                         |
| Protected, RIPAS=DESTROYED | Never                                                    | Always                                           | Never                                      | Always                                                        |
| Unprotected                | Host can inject SEA following REC exit due to Data Abort | When HIPAS=UNASSIGNED_NS                         | Always (SEA)                               | Never                                                         |
| Outside Realm IPA space    | Always (Address Size Fault)                              | Never                                            | Always (Address Size Fault)                | Never                                                         |

## See also:

- A4.2.3 REC entry following REC exit due to Data Abort

## A5.2.10 Cache maintenance operations

- RTZQDY A data cache invalidate by set / way instruction executed by a Realm either has no effect, or performs a data cache clean and invalidate.
- XXZRDW This is to ensure that a Realm cannot invalidate a cache line owned by another Realm.
- UVQMTB Arm expects that the RMM will set HCR\_EL2.VM == '1' , which causes a data cache invalidate instruction executed at EL1 to perform a data cache clean and invalidate.