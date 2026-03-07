## D1.5 Realm memory management flows

This section contains flows which relate to management of Realm memory.

See also:

- [Chapter A5 Realm memory management](rmm-A5.md)

## D1.5.1 Add memory to Active Realm flow

The following diagram shows the flow for adding memory to a Realm whose state is REALM\_ACTIVE.

To add memory to a Realm whose state is REALM\_ACTIVE, the Host must:

- Delegate a destination Granule ( dst ).
- Specify the Protected IPA at which the dst Granule will be mapped in the Realm's IPA space.
- Ensure that the level 3 RTT which contains the RTTE identified by the Protected IPA has been created.

Once a given Protected IPA has been populated with unknown content, it cannot be repopulated.

Figure D1.15: Add memory to active Realm flow

<!-- image -->


## See also:

- [A2.2.5 Realm lifecycle](rmm-A2.2.md#a225-realm-lifecycle)
- [Chapter A5 Realm memory management](rmm-A5.md)
- [B4.5.17 RMI\_GRANULE\_RANGE\_DELEGATE command](rmm-B4.5.17.md)
- [B4.5.65 RMI\_RTT\_DATA\_MAP command](rmm-B4.5.65.md)

## D1.5.2 NS memory flow

The following diagram describes how NS memory can be mapped into a Realm.

Figure D1.16: NS memory mapping flow

<!-- image -->

## See also:

- [Chapter A5 Realm memory management](rmm-A5.md)

- [B4.5.77 RMI\_RTT\_UNPROT\_MAP command](rmm-B4.5.77.md)
- [B4.5.78 RMI\_RTT\_UNPROT\_UNMAP command](rmm-B4.5.78.md)

## D1.5.3 RIPAS change flow

The following diagram describes how a Realm requests a RIPAS change, and how that request is handled by the Host.

- The Realm calls RSI\_IPA\_STATE\_SET to request a RIPAS change for IPA range [base, top) .
- This causes a REC exit due to RIPAS change pending.

On taking a REC exit due to RIPAS change pending, the Host does the following:

- Reads the region base and top addresses from the RmiRecExit object.
- Applies the requested RIPAS change to an IPA range starting from the base of the target region, and extending no further than the top of the target region.
- Calls RMI\_REC\_ENTER to re-enter the REC.

The Realm observes in X1 the top of the region for which the RIPAS change was applied.

Figure D1.17: RIPAS change flow

<!-- image -->

## See also:

- [A5.4 RIPAS change](rmm-A5.4.md)
- [B4.5.51 RMI\_REC\_ENTER command](rmm-B4.5.51.md)
- [B4.5.75 RMI\_RTT\_SET\_RIPAS command](rmm-B4.5.75.md)
- [B5.4.7 RSI\_IPA\_STATE\_SET command](rmm-B5.4.7.md)
- [D2.2 Realm shared memory protocol flow](rmm-D2.md#d22-realm-shared-memory-protocol-flow)

## D1.5.4 S2AP change flow

The following diagram describes how a Realm requests a S2AP change, and how that request is handled by the Host.

- The Realm calls RSI\_MEM\_SET\_PERM\_INDEX to request an S2AP change for IPA range [base, top) .
- This causes a REC exit due to S2AP change pending.

On taking a REC exit due to S2AP change pending, the Host does the following:

- Reads the region base and top addresses from the RmiRecExit object.
- Applies the requested S2AP change to an IPA range starting from the base of the target region, and extending no further than the top of the target region.
- Calls RMI\_REC\_ENTER to re-enter the REC.

The Realm observes in X1 the top of the region for which the S2AP change was applied.

Figure D1.18: S2AP change flow

<!-- image -->

## See also:

- [A10.3.2.3 Stage 2 Access Permissions change within a multi-Plane Realm](rmm-A10.3.md#a10323-stage-2-access-permissions-change-within-a-multi-plane-realm)
- [B4.5.51 RMI\_REC\_ENTER command](rmm-B4.5.51.md)
- [B4.5.76 RMI\_RTT\_SET\_S2AP command](rmm-B4.5.76.md)
- [B5.4.11 RSI\_MEM\_SET\_PERM\_INDEX command](rmm-B5.4.11.md)