## D1.2 Realm lifecycle flows

This section contains flows which relate to the Realm lifecycle.

See also:

- [A2.2.5 Realm lifecycle](rmm-A2.2.md#a225-realm-lifecycle)

## D1.2.1 Realm creation flow

The following diagram shows the flow for creating a Realm.

To create a Realm, the Host must allocate and delegate two Granules:

- rd to store the Realm Descriptor
- rtt which will be the starting level Realm Translation Table (RTT)

The Host also provides an NS Granule ( params ) containing Realm creation parameters.

Figure D1.3: Realm creation flow

<!-- image -->

## See also:

- [B4.3.4 Object creation and destruction](rmm-B4.3.md#b434-object-creation-and-destruction)
- [B4.5.17 RMI\_GRANULE\_RANGE\_DELEGATE command](rmm-B4.5.17.md)
- [B4.5.46 RMI\_REALM\_CREATE command](rmm-B4.5.46.md)
- [D1.2.5 Realm destruction flow](rmm-D1.2.md#d125-realm-destruction-flow)

## D1.2.2 Realm Translation Table creation flow

The following diagram shows the flow for populating the Realm Translation Tables (RTTs).

The starting level Realm Translation Tables (RTTs) are provided at Realm creation time.

Subsequent levels of RTT are added using the RMI\_RTT\_CREATE command.

Figure D1.4: RTT creation flow

<!-- image -->


See also:

- [Chapter A5 Realm memory management](rmm-A5.md)
- [B4.5.64 RMI\_RTT\_CREATE command](rmm-B4.5.64.md)
- [D1.2.1 Realm creation flow](rmm-D1.2.md#d121-realm-creation-flow)
- [D1.2.3 Initialize memory of New Realm flow](rmm-D1.2.md#d123-initialize-memory-of-new-realm-flow)

## D1.2.3 Initialize memory of New Realm flow

Immediately following Realm creation, every page in the Protected IPA space has its RIPAS set to RIPAS\_EMPTY. There are two ways in which the Host can set the RIPAS of a given page of Protected IPA space to RIPAS\_RAM:

1. Change the RIPAS by executing RMI\_RTT\_INIT\_RIPAS, but do not populate the contents of the page. The RIM is extended to reflect the RIPAS change.
2. Both change the RIPAS and populate the page with contents provided by the Host, by executing RMI\_RTT\_DATA\_MAP\_INIT. The RIM is extended to reflect the contents added by the Host.

Once the Host has performed either of these actions for a given page of Protected IPA space, that page cannot be further modified prior to Realm activation.

The following diagram shows the flow for initializing the RIPAS without providing contents.

<!-- image -->


Figure D1.5: RIPAS initialization flow

The following diagram shows the flow for populating the page with contents provided by the Host.

To do this, the Host must:

- Delegate a destination Granule ( dst ).
- Provide an NS Granule ( src ), whose contents will be copied into the destination Granule.
- Specify the Protected IPA ipa at which the dst Granule should be mapped in the Realm's IPA space.
- Ensure that the level 3 RTT which contains the RTTE identified by the Protected IPA has been created.

Once the Data Granule has been created, the src Granule can be reallocated by the Host.

## See also:

- [A2.3.6 Granule state](rmm-A2.3.md#a236-granule-state)
- [A5.2.2 Realm IPA state](rmm-A5.1.md#a522-realm-ipa-state)


- [A7.1.1 Realm Initial Measurement](rmm-A7.1.md#a711-realm-initial-measurement)
- [B4.5.17 RMI\_GRANULE\_RANGE\_DELEGATE command](rmm-B4.5.17.md)
- [B4.5.66 RMI\_RTT\_DATA\_MAP\_INIT command](rmm-B4.5.66.md)
- [B4.5.73 RMI\_RTT\_INIT\_RIPAS command](rmm-B4.5.73.md)
- [D1.2.1 Realm creation flow](rmm-D1.2.md#d121-realm-creation-flow)
- [D1.2.2 Realm Translation Table creation flow](rmm-D1.2.md#d122-realm-translation-table-creation-flow)
- [D1.2.5 Realm destruction flow](rmm-D1.2.md#d125-realm-destruction-flow)

## D1.2.4 REC creation flow

The following diagram shows the flow for creating a REC during Realm creation.

Once the REC has been created, the params Granule can be reallocated by the Host.

Figure D1.6: Realm data creation flow

<!-- image -->

Figure D1.7: REC creation flow

<!-- image -->

## See also:

- [B4.3.4 Object creation and destruction](rmm-B4.3.md#b434-object-creation-and-destruction)
- [B4.5.17 RMI\_GRANULE\_RANGE\_DELEGATE command](rmm-B4.5.17.md)
- [B4.5.49 RMI\_REC\_CREATE command](rmm-B4.5.49.md)
- [D1.2.1 Realm creation flow](rmm-D1.2.md#d121-realm-creation-flow)
- [D1.2.5 Realm destruction flow](rmm-D1.2.md#d125-realm-destruction-flow)

## D1.2.5 Realm destruction flow

The following diagram shows the flow for destroying a Realm.

To destroy a Realm, the Host must perform the following actions:

1a. Ensure that no REC owned by the Realm is running.

1b. Terminate the Realm, which causes it to enter REALM\_ZOMBIE state. Realm termination can result in an intermediate state, therefore requiring multiple calls to complete the destruction. On entry to REALM\_ZOMBIE state, the RMM ensures that all DMA initiated by the Realm has stopped.

1c. If the system has any attached CMEM devices, perform necessary MEC maintenance.

2. Make the Realm non-live. This is done by destroying (in any order) the objects which are associated with the Realm:
- Data Granules
- REC
- RTT
- VDEV
- VSMMU
3. Destroy the Realm. This is an operation which can result in an intermediate state, therefore requiring multiple calls to complete the destruction.

Steps 1 and 2 above can be performed in either order.

Once each object (DATA, REC, RTT and RD) has been destroyed, the corresponding Granules can be undelegated and reallocated by the Host.


Figure D1.8: Realm destruction flow (part 1 of 2)

<!-- image -->

## See also:

- [A2.2.4 Realm liveness](rmm-A2.2.md#a224-realm-liveness)
- [A11.1.2 MEC and CMEM devices](rmm-A11.md#a1112-mec-and-cmem-devices)
- [B4.3.2 Stateful RMI operations](rmm-B4.3.md#b432-stateful-rmi-operations)
- [B4.3.4 Object creation and destruction](rmm-B4.3.md#b434-object-creation-and-destruction)
- [B4.5.18 RMI\_GRANULE\_RANGE\_UNDELEGATE command](rmm-B4.5.18.md)
- [B4.5.47 RMI\_REALM\_DESTROY command](rmm-B4.5.47.md)
- [B4.5.48 RMI\_REALM\_TERMINATE command](rmm-B4.5.48.md)
- [B4.5.50 RMI\_REC\_DESTROY command](rmm-B4.5.50.md)
- [B4.5.67 RMI\_RTT\_DATA\_UNMAP command](rmm-B4.5.67.md)
- [B4.5.68 RMI\_RTT\_DESTROY command](rmm-B4.5.68.md)
- [B4.5.83 RMI\_VDEV\_DESTROY command](rmm-B4.5.83.md)
- [B4.5.96 RMI\_VSMMU\_DESTROY command](rmm-B4.5.96.md)
- [D1.2.1 Realm creation flow](rmm-D1.2.md#d121-realm-creation-flow)

Figure D1.9: Realm destruction flow (part 2 of 2)

<!-- image -->