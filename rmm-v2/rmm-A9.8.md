## A9.8 Virtual SMMU

- A Virtual SMMU (VSMMU) object stores the state of a Arm VSMMU which is emulated by the RMM.
- For every PSMMU used by one or more device functions which are assigned to a Realm, if one or more of those device functions require stage 1 translation then a corresponding VSMMU must be created.
- A VSMMU can only be created while the Realm state is NEW.
- A VSMMU is created and bound to a Realm by execution of RMI\_VSMMU\_CREATE. This command only permits VSMMU creation while the Realm state is NEW.
- Supported VSMMU features can be discovered by calling RMI\_VSMMU\_FEATURES.
- The Host provides the VSMMU AIDR and IDR values when executing RMI\_VSMMU\_CREATE.
- RMI\_VSMMU\_CREATE fails if the provided AIDR or IDR values are not supported.
- The encoding of the AIDR and IDR values is as specified by the Non-secure world SMMU architecture, which in some cases differ from the corresponding Realm world encodings.
- A VSMMU is destroyed by execution of RMI\_VSMMU\_DESTROY.
- A VSMMU is bound to a VDEV by execution of RMI\_VDEV\_CREATE, with RmiVdevFlags::VSMMU set.
- A VSMMU is unbound from a VDEV by execution of RMI\_VDEV\_DESTROY. IQWBJH Mappings from Realm Protected IPA space to a VSMMU object are created by execution of RMI\_RTT\_ARCH\_DEV\_MAP. This command only permits such mappings to be created within the register IPA range specified on creation of the VSMMU object. This causes the HIPAS to change from HIPAS\_VOID to HIPAS\_ARCH\_DEV. IHZHZY Mappings from Realm Protected IPA space to a VSMMU object are removed by execution of RMI\_RTT\_ARCH\_DEV\_UNMAP. See also: · Arm System Memory Management Unit Architecture Specification [22] · A9.8.3 VSMMU liveness · A9.8.4 VSMMU validation
- B4.5.55 RMI\_RTT\_ARCH\_DEV\_MAP command
- B4.5.56 RMI\_RTT\_ARCH\_DEV\_UNMAP command
- B4.5.82 RMI\_VDEV\_CREATE command
- B4.5.83 RMI\_VDEV\_DESTROY command
- B4.5.95 RMI\_VSMMU\_CREATE command
- B4.5.96 RMI\_VSMMU\_DESTROY command
- B4.5.99 RMI\_VSMMU\_FEATURES command

## A9.8.1 VSMMU attributes

- The attributes of a VSMMU are summarized in the following table.

| Name     | Type          | Description                                              |
|----------|---------------|----------------------------------------------------------|
| state    | RmmVsmmuState | State of the VSMMU                                       |
| realm    | Address       | PA of RD of Realm which owns this VSMMU                  |
| reg_base | Address       | Base IPA of register base in Realm's Protected IPA space |
| reg_top  | Address       | Top IPA of register base in Realm's Protected IPA space  |


| Name       | Type             | Description              |
|------------|------------------|--------------------------|
| aidr       | Bits64           | SMMU_AIDR register value |
| idr        | Bits64[7]        | SMMU_IDR register values |
| msi_config | RmmSmmuMsiConfig | MSI configuration        |

The Host provides the VSMMU register IPA range when executing RMI\_VSMMU\_CREATE.

See also:

- [B4.5.95 RMI\_VSMMU\_CREATE command](rmm-B4.5.95.md)

## A9.8.2 VSMMU lifecycle

## A9.8.2.1 States

The states of a VSMMU are listed below.

| State          | Description                                |
|----------------|--------------------------------------------|
| VSMMU_INACTIVE | VSMMU has not been activated by the Realm. |
| VSMMU_ACTIVE   | VSMMU has been activated by the Realm.     |

Realm access to a VSMMU whose state is not VSMMU\_ACTIVE results in an UNKNOWN exception taken to the Realm.

## A9.8.2.2 State transitions

On creation by execution of RMI\_VSMMU\_CREATE, the initial state of a VSMMU is VSMMU\_INACTIVE.

Successful execution of RSI\_ARCH\_DEV\_ACTIVATE with the base input value matching the base IPA of the VSMMU register space causes the state of the VSMMU to transition to VSMMU\_ACTIVE.


Successful execution of RSI\_ARCH\_DEV\_ACTIVATE with the base input value matching the base IPA of the VSMMU register space causes the RIPAS of all IPAs within its MMIO interface to transition to RIPAS\_DEV.

Successful execution of RMI\_RTT\_ARCH\_DEV\_UNMAP causes the state of the VSMMU to transition to VSMMU\_INACTIVE.

Permitted VSMMU state transitions are shown in the following table. The rightmost column lists the events which can cause the corresponding state transition.

A transition from the pseudo-state NULL represents creation of a VSMMU object. A transition to the pseudo-state NULL represents destruction of a VSMMU object.

| From state     | To state       | Events                 |
|----------------|----------------|------------------------|
| NULL           | VSMMU_INACTIVE | RMI_VSMMU_CREATE       |
| VSMMU_INACTIVE | VSMMU_ACTIVE   | RSI_ARCH_DEV_ACTIVATE  |
| VSMMU_ACTIVE   | VSMMU_INACTIVE | RMI_RTT_ARCH_DEV_UNMAP |
| VSMMU_INACTIVE | NULL           | RMI_VSMMU_DESTROY      |
| VSMMU_ACTIVE   | NULL           | RMI_VSMMU_DESTROY      |

## See also:

- [B4.5.56 RMI\_RTT\_ARCH\_DEV\_UNMAP command](rmm-B4.5.56.md)
- [B4.5.95 RMI\_VSMMU\_CREATE command](rmm-B4.5.95.md)
- [B4.5.96 RMI\_VSMMU\_DESTROY command](rmm-B4.5.96.md)
- [B5.4.1 RSI\_ARCH\_DEV\_ACTIVATE command](rmm-B5.4.1.md)

## A9.8.3 VSMMU liveness


VSMMU liveness is a property which means that there exists one or more mappings from Realm Protected IPA space to the VSMMU object.


If a VSMMU is live, it cannot be destroyed.

## See also:

- [A9.8.2 VSMMU lifecycle](rmm-A9.8.md#a982-vsmmu-lifecycle)
- [B3.235 VsmmuIsLive function](rmm-B3.md#b3235-vsmmuislive-function)
- [B4.5.96 RMI\_VSMMU\_DESTROY command](rmm-B4.5.96.md)

## A9.8.4 VSMMU validation

- The Realm queries whether an IPA is the base address of a VSMMU by execution of RSI\_VSMMU\_GET\_INFO.
- The Realm activates the register interface of a VSMMU by execution of RSI\_ARCH\_DEV\_ACTIVATE. This causes the RIPAS of the IPA range to change from RIPAS\_EMPTY to RIPAS\_DEV.

On execution of RSI\_ARCH\_DEV\_ACTIVATE, if the RMM reaches an RTTE within the IPA range whose HIPAS is not HIPAS\_ARCH\_DEV then the command fails with RSI\_ERROR\_DEVICE.

The attributes of a VSMMU are guaranteed not to change between execution of RSI\_VSMMU\_GET\_INFO and RSI\_ARCH\_DEV\_ACTIVATE.


The programming model for validating and activating a VSMMU is shown in the following pseudocode:

```
int realm_validate_vsmmu(uint64_t base, uint64_t top) { uint64_t new_base; RsiResponse response; int ret = RSI_SUCCESS; // Check whether "base" identifies a VSMMU ret = rsi_vsmmu_get_info(base); if (ret != RSI_SUCCESS) { return ret; } // Activate the VSMMU register interface while (base != top) { ret = RSI_ARCH_DEV_ACTIVATE(base, top, if (ret != RSI_SUCCESS) { return ret; } base = new_base; } return RSI_SUCCESS; }
```

```
&new_base);
```

Setup of an VSMMU is illustrated in the following sequence diagram.

Figure A9.17: VSMMU setup

<!-- image -->

RSI\_VDEV\_GET\_INFO reports to the Realm whether the VDEV is associated with a VSMMU. If so, the VSMMU base address and vSID are provided. This allows the Realm to check that the VDEV is associated with the expected VSMMU and vSID.

See also:

- [A9.8.2 VSMMU lifecycle](rmm-A9.8.md#a982-vsmmu-lifecycle)


- [B5.4.1 RSI\_ARCH\_DEV\_ACTIVATE command](rmm-B5.4.1.md)
- [B5.4.19 RSI\_VDEV\_GET\_INFO command](rmm-B5.4.19.md)
- [B5.4.23 RSI\_VSMMU\_GET\_INFO command](rmm-B5.4.23.md)

## A9.8.5 VSMMU commands

This section describes how commands provided to a VSMMU via the virtual Command Queue are handled.

- When a VSMMU Command Queue becomes non-empty due to the Realm enqueuing a command, a REC exit due to VSMMU command results.
- Handling of a VSMMU command is described below.

## 1. Realm enqueues command to VSMMU Command Queue

In response, the RMM performs a REC exit due to VSMMU command.

## 2. Host asks RMM to read VSMMU Command Queue

The Host calles RMI\_VSMMU\_CMD\_GET, requesting the RMM to inspect the first entry in the VSMMU Command Queue.

The return values from this command include flags which inform the Host of the action which needs to be taken next. The following sections describe each flag.

## 2a) Complete command on PSMMU

If the 'cmd\_complete' flag is set then the Host calls RMI\_VSMMU\_CMD\_COMPLETE, passing the VSMMU along with the corresponding RD, PDEV and VDEV objects.

The RMM checks the PSMMU Command Queue. If that queue has space then the RMM consumes the VSMMU Command Queue entry and enqueues a corresponding entry into the PSMMU Command Queue.

If the PSMMU Command Queue is full then a 'busy' error is returned to the Host.

## 2b) Inject IRQ for CMDQ

If the 'irq' flag is set then the Host injects a vIRQ into the Realm.

- Handling of a VSMMU command is illustrated in the following sequence diagram.


## See also:

- [A4.3.15 REC exit due to VSMMU command](rmm-A4.3.md#a4315-rec-exit-due-to-vsmmu-command)
- [B4.5.93 RMI\_VSMMU\_CMD\_COMPLETE command](rmm-B4.5.93.md)
- [B4.5.94 RMI\_VSMMU\_CMD\_GET command](rmm-B4.5.94.md)

## A9.8.6 Page Request Interface events


This section describes how Page Request Interface (PRI) events are delivered to a Realm which has an assigned VSMMU.

## A9.8.6.1 Page Request Interface flow

Delivery and handling of a PRI event is described below.

## 1. Device sends page request to PSMMU

The device issues an ATS request, which the SMMU completes, indicating that stage 1 translation failed.

In response, the device sends a PRI Page Request (PPR) to the SMMU.

## 2. PSMMU recieves page request

The PSMMU enqueues the PPR into the physical SMMU PRI queue (pPRIQ).

3. If pPRIQ transitioned from empty to non-empty, PSMMU raises interrupt, which Host forwards to RMM

On taking the PRI interrupt, the Host calls the RMI\_PSMMU\_IRQ\_NOTIFY command.

## 4. RMM receives PSMMU page request

The RMM reads the PPR entry from the pPRIQ. At this point, the RMM does not advance the PSMMU consumer counter.

The RMM sets a per-PSMMU flag to indicate that a PPR is pending.

Figure A9.18: Handling of a VSMMU command

<!-- image -->

The RMM returns control to the Host, passing a flag which indicates that an event should be notified to the corresponding SMMU, and the physical Stream ID (pSID).

## 5. Host maps page request from PSMMU to VSMMU

If the Host fails to map the (PSMMU, pSID) tuple, it calls the RMI\_PSMMU\_EVENT\_DISCARD command. The RMMclears the 'PPR pending' flag on the PSMMU, and advances the PSMMU consumer counter. In this case, this is the end of the flow.

If the Host successfully maps the (PSMMU, pSID) tuple to the corresponding (RD, VSMMU, VDEV) values. It then calls the RMI\_VSMMU\_EVENT\_NOTIFY command, passing the latter.

## 6. RMM inserts page request into VSMMU

The RMM checks that the 'PPR pending' flag is set on the PSMMU. It then peeks the pPRIQ to check that the top entry matches incoming parameters.

The RMM then attempts to copy the PPR into the virtual SMMU PRI queue (vPRIQ), with the SID field set to the virtual Stream ID (vSID) from the VDEV provided by the Host. This copy operation has the following possible outcomes:

## (a) The vPRIQ is not accessible because HIPAS is not HIPAS\_DATA

The RMM returns the faulting IPA to the Host.

(b) The vPRIQ is not accessible because RIPAS is not RIPAS\_RAM, or S2AP does not permit write access The RMM sets SMMU\_R\_GERROR.PRIQ\_ABT\_ERR in the VSMMU. The RMM returns control to the Host, passing a flag which indicates that a virtual IRQ should be injected into the Realm, with the MSI address and data values for the GERROR interrupt which the Realm programmed into the VSMMU. (c) The vPRIQ has not been configured The RMM silently drops the PPR. The RMM returns control to the Host with no flag set. (d) The vPRIQ is full

The RMM reads STE.PPAR to determine whether it should send a PASID value to the PSMMU.

If the PPR is marked LAST == 0 , the RMM silently drops the PPR.

If the PPR is marked LAST == 1 , the RMM sends CMD\_PRI\_RESP(SUCCESS) to the PSMMU. In response, the device may issue another PPR. If the Realm has executed before the next PPR is sent, its actions may have resulted in space becoming available in the vPRIQ.

The RMM returns control to the Host with no flag set.

## (e) The PPR was successfully copied into the vPRIQ

The RMM returns control to the Host, passing a flag which indicates that a virtual IRQ should be injected into the Realm, with the MSI address and data values for the PRIQ interrupt which the Realm programmed into the VSMMU.

## 7. Host injects virtual interrupt into Realm

The Host determines which REC should receive the PRI vIRQ, writes List Register values into the REC entry structure, and calls RMI\_REC\_ENTER.

## 8. Realm handles VSMMU page request

On taking the PRI interrupt, the Realm reads the PPR from the vPRIQ. It then creates the required stage 1 mapping(s) and writes CMD\_PRI\_RESP into the virtual SMMU Command Queue (vCMDQ). This traps to the RMM.

## 9. RMM receives VSMMU page response

The RMM performs a REC exit due to VSMMU command, passing the VSMMU IPA.

## 10. Host maps page response from VSMMU to PSMMU

The Host calls RMI\_VSMMU\_CMD\_GET, passing the VSMMU object. The return values include the vSID.

The Host maps the (RD, vSMMU, vSID) tuple to the corresponding (PSMMU, pSID) values. It then calls the RMI\_VSMMU\_EVENT\_COMPLETE command, passing the latter.

## 11. RMM sends page response to PSMMU

The RMM constructs a PPR using the values saved in the REC, and attempts to write it to the physical SMMU Command Queue (pCMDQ).

If the pCMDQ is full, the RMM returns RMI\_BUSY to the Host.

## 12. PSMMU sends page response to device

If the PPR write was successful, the PSMMU consumes the command from the pCMDQ. It sends the Page Request Group (PRG) response to the device.

The device reissues the ATS request, which the SMMU completes with success, returning the translated address to the device.

Delivery and handling of a PRI event is illustrated in the following sequence diagram.


Figure A9.19: Delivery and handling of a PRI event (part 1 of 2)

<!-- image -->

## See also:

- [A4.3.15 REC exit due to VSMMU command](rmm-A4.3.md#a4315-rec-exit-due-to-vsmmu-command)
- [B4.5.41 RMI\_PSMMU\_EVENT\_DISCARD command](rmm-B4.5.41.md)
- [B4.5.42 RMI\_PSMMU\_IRQ\_NOTIFY command](rmm-B4.5.42.md)
- [B4.5.51 RMI\_REC\_ENTER command](rmm-B4.5.51.md)
- [B4.5.97 RMI\_VSMMU\_EVENT\_COMPLETE command](rmm-B4.5.97.md)
- [B4.5.98 RMI\_VSMMU\_EVENT\_NOTIFY command](rmm-B4.5.98.md)

Figure A9.20: Delivery and handling of a PRI event (part 2 of 2)

<!-- image -->