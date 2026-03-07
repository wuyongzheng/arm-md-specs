## A9.7 Physical SMMU

- A physical device which contains functions that can be assigned to Realms must access memory via a physical SMMU(PSMMU).
- A PSMMU is identified by the base physical address of SMMUv3\_PAGE\_0 for the Non-secure SMMU instance. See also:
- Arm System Memory Management Unit Architecture Specification [22]
- A9.8 Virtual SMMU

## A9.7.1 PSMMU object

## A9.7.1.1 PSMMU attributes

The attributes of a PSMMU are summarized in the following table.

| Name        | Type             | Description                                                                          |
|-------------|------------------|--------------------------------------------------------------------------------------|
| state       | RmmPsmmuState    | State of the PSMMU                                                                   |
| sid_size    | UInt64            StreamID size in bits. This is read from the SMMU_IDR1.SIDSIZE register field. |
| feat_msi    | RmmFeature       | Whether the PSMMU supports MSI                                                       |
| feat_ats    | RmmFeature       | Whether the PSMMU supports ATS                                                       |
| feat_pri    | RmmFeature       | Whether the PSMMU supports PRI                                                       |
| msi_config  | RmmSmmuMsiConfig | MSI configuration                                                                    |
| ppr_pending | RmmBoolean       | Whether a PRI Page Request is pending on this PSMMU                                  |

At platform boot, the state of a PSMMU is INACTIVE.

- The state of a PSMMU is transitioned from INACTIVE to ACTIVE by execution of RMI\_PSMMU\_ACTIVATE.
- The state of a PSMMU is transitioned from ACTIVE to INACTIVE by execution of RMI\_PSMMU\_DEACTIVATE. See also:
- B4.5.39 RMI\_PSMMU\_ACTIVATE command
- B4.5.40 RMI\_PSMMU\_DEACTIVATE command

## A9.7.1.2 PSMMU lifecycle

## A9.7.1.2.1 States

The states of a PSMMU are listed below.

| State          | Description                   |
|----------------|-------------------------------|
| PSMMU_INACTIVE | PSMMU has not been activated. |
| PSMMU_ACTIVE   | PSMMU has been activated.     |

## A9.7.2 PSMMU activation

- On execution of RMI\_PSMMU\_ACTIVATE, if the implementation requires memory to be donated then the 'donating memory to a Stateful RMI Operation (SRO)' flow is followed.
- The memory required by the implementation for management of PSMMU includes the Level 1 Stream Table and queues.
- If ATS is enabled for the PSMMU, RMI\_PSMMU\_ACTIVATE fails unless the Level 0 DPT has been fully created before the RMI\_PSMMU\_ACTIVATE is called.
- For a PSMMU which supports MSI, execution of RMI\_PSMMU\_ACTIVATE initializes the values of the MSI address and data attributes.

See also:

- [A9.7.5 Device Permission Table](rmm-A9.7.md#a975-device-permission-table)
- [B4.3.2.2 Donating memory to an SRO](rmm-B4.3.md#b4322-donating-memory-to-an-sro)
- [B4.5.39 RMI\_PSMMU\_ACTIVATE command](rmm-B4.5.39.md)

## A9.7.3 PSMMU deactivation

- On execution of RMI\_PSMMU\_DEACTIVATE, if memory was donated when the PSMMU was activated then it is reclaimed via the 'reclaiming memory from a Stateful RMI Operation (SRO)' flow.

See also:

- [A9.7.5 Device Permission Table](rmm-A9.7.md#a975-device-permission-table)
- [B4.3.2.3 Reclaiming memory from an SRO](rmm-B4.3.md#b4323-reclaiming-memory-from-an-sro)
- [B4.5.40 RMI\_PSMMU\_DEACTIVATE command](rmm-B4.5.40.md)

## A9.7.4 PSMMU Stream Tables

- A PSMMU Stream Table is associated with a given PSMMU instance.
- A PSMMU Stream Table has up to two levels. Level 2 is required if the PSMMU implements more than 64 Stream IDs.
- Both levels of a PSMMU Stream Table are allocated at runtime from memory which has been delegated to the RMMfrom DRAM.


- The size of a PSMMU Level 1 Stream Table is determined by its sid\_size and split attributes and may span multiple Granules.
- The size of a PSMMU Level 2 Stream Table is one Granule.
- A PSMMU Level 2 Stream Table is created by execution of RMI\_PSMMU\_ST\_L2\_CREATE.
- On execution of RMI\_PSMMU\_ST\_L2\_CREATE, the 'donating memory to a Stateful RMI Operation (SRO)' flow is followed.
- A PSMMU Level 2 Stream Table is destroyed by execution of RMI\_PSMMU\_ST\_L2\_DESTROY.
- On execution of RMI\_PSMMU\_ST\_L2\_DESTROY, the 'reclaiming memory from a Stateful RMI Operation (SRO)' flow is followed.
- A Level 1 Stream Table is live if any of its entries points to a Level 2 Stream Table.
- The function PsmmuL1StIsLive() is used to evaluate whether a Level 1 Stream Table is live.
- Execution of RMI\_PSMMU\_DEACTIVATE fails if the Level 1 Stream Table is live.
- A Level 2 Stream Table is live if any of its entries corresponds to a VDEV.
- The function PsmmuL2StIsLive() is used to evaluate whether a Level 2 Stream Table is live.

- Execution of RMI\_PSMMU\_ST\_L2\_DESTROY fails if the Level 2 Stream Table is live.

See also:

- [A9.7.2 PSMMU activation](rmm-A9.7.md#a972-psmmu-activation)
- [A9.7.3 PSMMU deactivation](rmm-A9.7.md#a973-psmmu-deactivation)
- [B3.93 PsmmuL1StIsLive function](rmm-B3.md#b393-psmmul1stislive-function)
- [B3.94 PsmmuL2StIsLive function](rmm-B3.md#b394-psmmul2stislive-function)
- [B4.3.2.2 Donating memory to an SRO](rmm-B4.3.md#b4322-donating-memory-to-an-sro)
- [B4.3.2.3 Reclaiming memory from an SRO](rmm-B4.3.md#b4323-reclaiming-memory-from-an-sro)
- [B4.5.43 RMI\_PSMMU\_ST\_L2\_CREATE command](rmm-B4.5.43.md)
- [B4.5.44 RMI\_PSMMU\_ST\_L2\_DESTROY command](rmm-B4.5.44.md)
- [B4.5.82 RMI\_VDEV\_CREATE command](rmm-B4.5.82.md)

## A9.7.5 Device Permission Table

- A DPT is a table, indexed by physical address, which indicates the VMID(s) which are permitted to access the corresponding physical location. Its purpose is to check that accesses to Realm PAS made by a device which stores translated addresses are permitted.
- A DPT is a system-wide singleton.
- A DPT is a two-level data structure.
- Both levels of a DPT are allocated at runtime from memory which has been delegated to the RMM.
- The DPT Granule size is equal to the RMM Granule size.
- A Level 0 DPT is created by execution of RMI\_DPT\_L0\_CREATE.
- On execution of RMI\_DPT\_L0\_CREATE, the 'donating memory to a Stateful RMI Operation (SRO)' flow is followed.
- Memory which is donated for the Level 0 DPT must satisfy alignment requirements specified in the SMMU architecture.
- A Level 0 DPT is destroyed by execution of RMI\_DPT\_L0\_DESTROY.
- On execution of RMI\_DPT\_L0\_DESTROY, the 'reclaiming memory from a Stateful RMI Operation (SRO)' flow is followed.


- A Level 1 DPT is created by execution of RMI\_DPT\_L1\_CREATE.
- On execution of RMI\_DPT\_L1\_CREATE, the 'donating memory to a Stateful RMI Operation (SRO)' flow is followed.
- A Level 1 DPT is destroyed by execution of RMI\_DPT\_L1\_DESTROY.
- On execution of RMI\_DPT\_L1\_DESTROY, the 'reclaiming memory from a Stateful RMI Operation (SRO)' flow is followed.
- Creation or destruction of Level 1 DPTs which describes different physical address regions may be performed concurrently.
- If ATS is enabled for a Realm then allocation of memory to the Realm by execution of RMI\_RTT\_DATA\_MAP\_INIT or RMI\_RTT\_DATA\_MAP fails if the corresponding Level 1 DPT has not been created .

See also:

- Arm System Memory Management Unit Architecture Specification [22]
- [B4.3.2.2 Donating memory to an SRO](rmm-B4.3.md#b4322-donating-memory-to-an-sro)
- [B4.3.2.3 Reclaiming memory from an SRO](rmm-B4.3.md#b4323-reclaiming-memory-from-an-sro)
- [B4.5.10 RMI\_DPT\_L0\_CREATE command](rmm-B4.5.10.md)
- [B4.5.11 RMI\_DPT\_L0\_DESTROY command](rmm-B4.5.11.md)

- [B4.5.12 RMI\_DPT\_L1\_CREATE command](rmm-B4.5.12.md)
- [B4.5.13 RMI\_DPT\_L1\_DESTROY command](rmm-B4.5.13.md)
- [B4.5.65 RMI\_RTT\_DATA\_MAP command](rmm-B4.5.65.md)
- [B4.5.66 RMI\_RTT\_DATA\_MAP\_INIT command](rmm-B4.5.66.md)

## A9.7.6 PSMMU interrupts

- For a PSMMU with MSI, configuration is provided by execution of RMI\_PSMMU\_ACTIVATE.
- For a PSMMU if wired interrupts are supported, no configuration is required from the RMM side. It is assumed that the RMM implementation will initialise SMMU\_*IRQ\_CFG0 registers to 0 to allow wired interrupts
- On taking a physical SMMU interrupt, the Host notifies the RMM by execution of RMI\_PSMMU\_IRQ\_NOTIFY. In response, the RMM may request the Host to inject a given virtual MSI into a specified Realm.
- The Host is expected to call RMI\_PSMMU\_IRQ\_NOTIFY in a loop until RmiPsmmuIrqOutputFlags::pending is RMI\_FALSE.

See also:

- [A9.8.2 VSMMU lifecycle](rmm-A9.8.md#a982-vsmmu-lifecycle)
- [B4.5.39 RMI\_PSMMU\_ACTIVATE command](rmm-B4.5.39.md)
- [B4.5.42 RMI\_PSMMU\_IRQ\_NOTIFY command](rmm-B4.5.42.md)

