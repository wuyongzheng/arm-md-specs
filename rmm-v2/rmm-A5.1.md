## A5.1 Realm memory management overview

Realm memory management can be viewed from one of two standpoints: the Realm and the Host.

From the Realm's point of view, the RMM provides security guarantees regarding the IPA space of the Realm and the memory which is mapped into it. These security guarantees are upheld via RSI commands which the Realm can execute in order to query the initial configuration and contents of its address space, and to modify properties of the address space at runtime.

From the Host's point of view, Realm memory management involves manipulating the stage 2 translation tables which describe the Realm's address space, and handling faults which are caused by Realm memory accesses. These operations are similar to those involved in managing the memory of a normal VM, but in the case of a Realm they are performed via execution of RMI commands.

See also:

- A5.2 Realm view of memory management
- A5.3 Host view of memory management

## A5.2 Realm view of memory management

This section describes memory management from the Realm's point of view.

## A5.2.1 Realm IPA space

- The IPA space of a Realm is divided into two halves: Protected IPA space and Unprotected IPA space.
- Software in a Realm should treat the most significant bit of an IPA as a protection attribute.
- A Protected IPA is an address in the lower half of a Realm's IPA space. The most significant bit of a Protected IPA is 0 .
- An Unprotected IPA is an address in the upper half of a Realm's IPA space. The most significant bit of an Unprotected IPA is 1 .

See also:

- A2.2.3 Realm attributes


- A3.3 Realm LPA2 and IPA width

## A5.2.2 Realm IPA state

- A Protected IPA has an associated Realm IPA state (RIPAS).

The RIPAS values are shown in the following table.

| Name            | Description                                                                    |
|-----------------|--------------------------------------------------------------------------------|
| RIPAS_DESTROYED | Address which is inaccessible to the Realm due to an action taken by the Host. |
| RIPAS_DEV       | Address where memory of an assigned Realm device is mapped.                    |
| RIPAS_EMPTY     | Address where no Realm resources are mapped.                                   |
| RIPAS_RAM       | Address where private code or data owned by the Realm is mapped.               |

RIPAS values are stored in leaf entries of the primary RTT.

The Realm can query the RIPAS of an IPA range by executing RSI\_IPA\_STATE\_GET.

See also:

- A5.6 Realm Translation Table
- Chapter A9 Realm device assignment
- B5.4.6 RSI\_IPA\_STATE\_GET command

## A5.2.3 Realm access to a Protected IPA

| R JVQQR   | Realm data access to a Protected IPA which is RIPAS_EMPTY causes a Synchronous External Abort taken to the Realm.                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R MKLSD   | Realm instruction fetch from a Protected IPA which is RIPAS_EMPTY causes a Synchronous External Abort taken to the Realm.                                                                                             |
| I QSQLF   | Realm data access to a Protected IPA which is RIPAS_RAM may cause a Synchronous External Abort taken to the Realm, if the access results in a Synchronous External Abort which is restartable or recoverable.         |
| I PGHBT   | Realm data access to a Protected IPA which is RIPAS_RAM can cause an REC exit due to Data Abort.                                                                                                                      |
| I FCJCP   | Realm instruction fetch from a Protected IPA which is RIPAS_RAM may cause a Synchronous External Abort taken to the Realm, if the access results in a Synchronous External Abort which is restartable or recoverable. |
| I XHKQY   | Realm instruction fetch from a Protected IPA which is RIPAS_RAM can cause a REC exit due to Instruction Abort.                                                                                                        |
| R CLVKF   | Realm data access to a Protected IPA which is RIPAS_DESTROYED causes a REC exit due to Data Abort.                                                                                                                    |
| R MZYQT   | Realm instruction fetch from a Protected IPA which is RIPAS_DESTROYED causes a REC exit due to Instruction Abort.                                                                                                     |
| I LSNTT   | Realm data access to a Protected IPA which is RIPAS_DEV may cause a Synchronous External Abort taken to the Realm, if the access results in a Synchronous External Abort which is restartable or recoverable.         |
| I XDXVV   | Realm data access to a Protected IPA which is RIPAS_DEV can cause an REC exit due to Data Abort.                                                                                                                      |
| R ZQTLP    Realm instruction fetch from a Protected IPA which is RIPAS_DEV causes a Synchronous External Abort taken to the Realm.                                                                                         |

See also:

- A4.3.4.2 REC exit due to Instruction Abort
- A4.3.4.3 REC exit due to Data Abort
- A5.2.4 RSI command access to a Protected IPA
- A5.2.8 Synchronous External Aborts
- A9.9.1 Device access to a Protected IPA

## A5.2.4 RSI command access to a Protected IPA

- Access by an RSI command to a Protected IPA which is RIPAS\_EMPTY causes the command to fail and return an error to the Realm.
- Access by an RSI command to a Protected IPA whose RIPAS is not RIPAS\_EMPTY is treated as a Realm data access to the same address, for the purposes of deciding whether the access causes a REC exit due to Data Abort.

See also:

- A5.2.3 Realm access to a Protected IPA

## A5.2.5 Changes to RIPAS while Realm state is REALM\_NEW

This section describes how the RIPAS of a Protected IPA can change while the Realm state is REALM\_NEW.

- For a Realm in the REALM\_NEW state, the RIPAS of a Protected IPA can change to RIPAS\_RAM due to Host execution of RMI\_RTT\_DATA\_MAP\_INIT or RMI\_RTT\_INIT\_RIPAS.
- For a Realm in the REALM\_NEW state, changing the RIPAS of a Protected IPA to RIPAS\_RAM causes the RIM to be updated.
- For a Realm in the REALM\_NEW state, the RIPAS of a Protected IPA can change to RIPAS\_DESTROYED due to Host execution of RMI\_RTT\_DATA\_UNMAP or RMI\_RTT\_DESTROY.
- For a Realm in the REALM\_NEW state, changing the RIPAS of a Protected IPA to RIPAS\_DESTROYED does not cause the RIM to be updated.

See also:

- A5.4 RIPAS change
- A7.1.1 Realm Initial Measurement
- B4.5.67 RMI\_RTT\_DATA\_UNMAP command
- B4.5.68 RMI\_RTT\_DESTROY command
- B4.5.73 RMI\_RTT\_INIT\_RIPAS command

## A5.2.6 Changes to RIPAS while Realm state is REALM\_ACTIVE

This section describes how the RIPAS of a Protected IPA can change while the Realm state is REALM\_ACTIVE.

- A Realm in the REALM\_ACTIVE state can request the RIPAS of a region of Protected IPA space to be changed to RIPAS\_EMPTY, RIPAS\_RAM or RIPAS\_DEV. IRXHXF ARealm in the REALM\_ACTIVE state cannot request the RIPAS of a region of Protected IPA space to be changed to RIPAS\_DESTROYED. IFRJJH For a Realm in the REALM\_ACTIVE state, the RIPAS of a Protected IPA can change to RIPAS\_EMPTY only in response to Realm execution of RSI\_IPA\_STATE\_SET. XHQLVY The fact that the Host cannot change the RIPAS of a Protected IPA to RIPAS\_EMPTY without the Realm having consented to this change prevents the Host from injecting an SEA at a Protected IPA which has been configured to have a RIPAS of RIPAS\_RAM, which could potentially trigger unexpected behavior in the Realm. IHNFYR For a Realm in the REALM\_ACTIVE state, the RIPAS of a Protected IPA can change to RIPAS\_RAM only in response to Realm execution of RSI\_IPA\_STATE\_SET.
- On execution of RSI\_IPA\_STATE\_SET, a Realm can optionally specify that the RIPAS change should only succeed if the current RIPAS is not RIPAS\_DESTROYED.
- An expected pattern for Realm creation is as follows:
1. Host populates an 'initial image' range of Realm IPA space with measured content:
- Host executes RMI\_RTT\_DATA\_MAP\_INIT, establishing a mapping to physical memory, changing RIPAS to RIPAS\_RAM and updating the RIM.
2. Host informs the Realm of the range of IPA space which should be considered by the Realm as DRAM. This is a superset of the IPA range populated in step 1. For unpopulated parts of this IPA range, the RIPAS is RIPAS\_EMPTY.
3. Realm executes RSI\_IPA\_STATE\_SET(ripas=RIPAS\_RAM) for the DRAM IPA range described to it in step 2. Following this command, the desired state is:
- a. For the initial image IPA range, the contents match those described by the RIM.
- b. For the entire DRAM IPA range, RIPAS is RIPAS\_RAM.

If at step 2, the Host were to execute RMI\_RTT\_DATA\_UNMAP on a page within the initial image IPA range, its RIPAS would change to RIPAS\_DESTROYED. The Host could then execute RMI\_RTT\_DATA\_MAP, with the result that contents of the initial image IPA range no longer match those described by the RIM.

By specifying at step 3 that the RIPAS change should only succeed if the current RIPAS is not RIPAS\_DESTROYED, the Realm is able to prevent loss of integrity within the initial image IPA range.

For a Realm in the REALM\_ACTIVE state, the RIPAS of a Protected IPA can change to RIPAS\_DEV only in response to Realm execution of RSI\_VDEV\_VALIDATE\_MAPPING.

For a Realm in the REALM\_ACTIVE state, the RIPAS of a Protected IPA can change to RIPAS\_DESTROYED due to Host execution of RMI\_RTT\_DATA\_UNMAP or RMI\_RTT\_DESTROY.

The result of changing the RIPAS of a Protected IPA to RIPAS\_DESTROYED is that subsequent Realm accesses to that address do not make forward progress. This is consistent with the principle that the RMM does not provide an availability guarantee to a Realm.

The following diagram summarizes RIPAS changes which can occur when the Realm state is REALM\_ACTIVE.

Figure A5.1: RIPAS changes which can occur when the Realm state is REALM\_ACTIVE

<!-- image -->

## See also:

- A5.4 RIPAS change
- A5.5 VDEV mapping validation
- B4.5.65 RMI\_RTT\_DATA\_MAP command
- B4.5.66 RMI\_RTT\_DATA\_MAP\_INIT command
- B4.5.67 RMI\_RTT\_DATA\_UNMAP command
- B4.5.68 RMI\_RTT\_DESTROY command
- B4.5.71 RMI\_RTT\_DEV\_VALIDATE command
- B4.5.73 RMI\_RTT\_INIT\_RIPAS command
- B5.4.7 RSI\_IPA\_STATE\_SET command
- B5.4.21 RSI\_VDEV\_VALIDATE\_MAPPING command

## A5.2.7 Realm access to an Unprotected IPA

- An access by a Realm to an Unprotected IPA can result in a Granule Protection Fault (GPF).

The RMM does not ensure that the GPT entry of a Granule mapped at an Unprotected IPA permits access via Non-secure PAS.


Realm software must be able to handle taking a GPF during access to an Unprotected IPA.

- Realm data access to an Unprotected IPA can cause a REC exit due to Data Abort.
- On taking a REC exit due to Data Abort at an Unprotected IPA, the Host can inject a Synchronous External Abort to the Realm.
- The Host can inject an SEA in response to an unexpected Realm data access to an Unprotected IPA.
- Realm data access to an Unprotected IPA which caused ESR\_EL2.ISS.ISV to be set to '1' can be emulated by the Host.
- Realm instruction fetch from an Unprotected IPA causes a Synchronous External Abort taken to the Realm. See also:
- A4.2.3 REC entry following REC exit due to Data Abort
- A4.3.4.3 REC exit due to Data Abort
- A4.4 Emulated Data Aborts
- A5.2.8 Synchronous External Aborts

## A5.2.8 Synchronous External Aborts

- When a Synchronous External Abort is taken to a Realm, ESR\_EL1.EA == '1' .
- A5.2.9 Realm access outside IPA space RGYVZQ If stage 1 translation is enabled, Realm access to an IPA which is greater than the IPA space of the Realm causes a stage 1 Address Size Fault taken to the Realm, with the fault status code indicating the level at which the fault occurred. RLSJJR If stage 1 translation is disabled, Realm access to an IPA which is greater than the IPA space of the Realm causes a stage 1 level 0 Address Size Fault taken to the Realm.

## A5.2.10 Summary of Realm IPA space properties

The following table summarizes the properties of Realm IPA space.

| Realm IPA                  | Data access causes abort to Realm?                                                                               | Data access causes REC exit due to Data Abort?            | Instruction fetch causes abort to Realm?                          | Instruction fetch causes REC exit due to Instruction Abort?   |
|----------------------------|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------------|---------------------------------------------------------------|
| Protected, RIPAS_EMPTY     | Always (SEA)                                                                                                     | Never                                                     | Always (SEA)                                                      | Never                                                         |
| Protected, RIPAS_RAM       | When access results in an SEA which is recoverable or restartable                                                | When HIPAS is not HIPAS_DATA                              | When access results in an SEA which is recoverable or restartable | When HIPAS is not HIPAS_DATA                                  |
| Protected, RIPAS_DEV       | When access results in an SEA which is recoverable or restartable                                                | When HIPAS is none of: • HIPAS_ARCH_DEV • HIPAS_NARCH_DEV | Always (SEA)                                                      | Never                                                         |
| Protected, RIPAS_DESTROYED | Never                                                                                                            | Always                                                    | Never                                                             | Always                                                        |
| Unprotected                | Host can inject SEA following REC exit due to Data Abort. GPF occurs if NS access is not permitted by GPT entry.  When access caused a stage 2 permission fault       | Always (SEA)                                                      | Never                                                         |
| Outside Realm IPA space    | Always (Address Size Fault)                                                                                      | Never                                                     | Always (Address Size Fault)                                       | Never                                                         |

## See also:

- A4.2.3 REC entry following REC exit due to Data Abort

## A5.2.11 Cache maintenance operations

- A data cache invalidate by set / way instruction executed by a Realm either has no effect, or performs a data cache clean and invalidate.
- This is to ensure that a Realm cannot invalidate a cache line owned by another Realm.
- Arm expects that the RMM will set HCR\_EL2.VM == '1' , which causes a data cache invalidate instruction executed at EL1 to perform a data cache clean and invalidate.