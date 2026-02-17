## D1.2 Realm lifecycle flows

This section contains flows which relate to the Realm lifecycle.

See also:

- A2.1.5 Realm lifecycle

## D1.2.1 Realm creation flow

The following diagram shows the flow for creating a Realm.

To create a Realm, the Host must allocate and delegate two Granules:

- rd to store the Realm Descriptor
- rtt which will be the starting level Realm Translation Table (RTT)

The Host also provides an NS Granule ( params ) containing Realm creation parameters.

<!-- image -->

## See also:

- B4.3.5 RMI\_GRANULE\_DELEGATE command
- B4.3.9 RMI\_REALM\_CREATE command
- D1.2.5 Realm destruction flow

## D1.2.2 Realm Translation Table creation flow

The following diagram shows the flow for populating the Realm Translation Tables (RTTs).

The starting level Realm Translation Tables (RTTs) are provided at Realm creation time.

Subsequent levels of RTT are added using the RMI\_RTT\_CREATE command. This can be performed when the state of the Realm is REALM\_NEW or REALM\_ACTIVE.

## See also:

- Chapter A5 Realm memory management
- B4.3.15 RMI\_RTT\_CREATE command
- D1.2.1 Realm creation flow
- D1.2.3 Initialize memory of New Realm flow

## D1.2.3 Initialize memory of New Realm flow

Immediately following Realm creation, every page in the Protected IPA space has its RIPAS set to EMPTY. There are two ways in which the Host can set the RIPAS of a given page of Protected IPA space to RAM:

1. Change the RIPAS by executing RMI\_RTT\_INIT\_RIPAS, but do not populate the contents of the page. The RIM is extended to reflect the RIPAS change.
2. Both change the RIPAS and populate the page with contents provided by the Host, by executing RMI\_DATA\_CREATE. The RIM is extended to reflect the contents added by the Host.

Once the Host has performed either of these actions for a given page of Protected IPA space, that page cannot be further modified prior to Realm activation.

The following diagram shows the flow for initializing the RIPAS without providing contents.

<!-- image -->

<!-- image -->

The following diagram shows the flow for populating the page with contents provided by the Host.

To do this, the Host must:

- Delegate a destination Granule ( dst ).
- Provide an NS Granule ( src ), whose contents will be copied into the destination Granule.
- Specify the Protected IPA ipa at which the dst Granule should be mapped in the Realm's IPA space.
- Ensure that the level 3 RTT which contains the RTTE identified by the Protected IPA has been created.

Once the Data Granule has been created, the src Granule can be reallocated by the Host.

## See also:

- A2.2.1 Granule attributes
- A5.2.2 Realm IPA state
- A7.1.1 Realm Initial Measurement
- B4.3.1 RMI\_DATA\_CREATE command
- B4.3.5 RMI\_GRANULE\_DELEGATE command
- B4.3.18 RMI\_RTT\_INIT\_RIPAS command
- D1.2.1 Realm creation flow
- D1.2.2 Realm Translation Table creation flow
- D1.2.5 Realm destruction flow

## D1.2.4 REC creation flow

The following diagram shows the flow for creating a REC during Realm creation.

To create a REC, the Host must:

- Delegate a destination Granule ( rec ).
- Query the number of auxiliary Granules required, by calling RMI\_REC\_AUX\_COUNT
- Delegate the required number of auxiliary Granules ( aux )
- Provide auxiliary Granule addresses, register values and REC activation status in an NS Granule ( params ).

Once the REC has been created, the params Granule can be reallocated by the Host.

<!-- image -->

See also:

<!-- image -->

- B4.3.5 RMI\_GRANULE\_DELEGATE command
- B4.3.11 RMI\_REC\_AUX\_COUNT command
- B4.3.12 RMI\_REC\_CREATE command
- D1.2.1 Realm creation flow
- D1.2.5 Realm destruction flow

## D1.2.5 Realm destruction flow

The following diagram shows the flow for destroying a Realm.

To destroy a Realm, the Host must first make the Realm non-live. This is done by destroying (in any order) the objects which are associated with the Realm:

- Data Granules
- RECs
- RTTs

Finally, the Realm itself can be destroyed.

Once each of these objects has been destroyed, the corresponding Granules can be undelegated and reallocated by the Host.

## See also:

- A2.1.4 Realm liveness
- B4.3.3 RMI\_DATA\_DESTROY command
- B4.3.6 RMI\_GRANULE\_UNDELEGATE command
- B4.3.10 RMI\_REALM\_DESTROY command
- B4.3.13 RMI\_REC\_DESTROY command
- D1.2.1 Realm creation flow

<!-- image -->