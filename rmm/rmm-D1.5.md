## D1.5 Realm memory management flows

This section contains flows which relate to management of Realm memory.

## See also:

- Chapter A5 Realm memory management

## D1.5.1 Add memory to Active Realm flow

The following diagram shows the flow for adding memory to a Realm whose state is REALM\_ACTIVE.

To add memory to a Realm whose state is REALM\_ACTIVE, the Host must:

- Delegate a destination Granule ( dst ).
- Specify the Protected IPA at which the dst Granule will be mapped in the Realm's IPA space.
- Ensure that the level 3 RTT which contains the RTTE identified by the Protected IPA has been created.

Once a given Protected IPA has been populated with unknown content, it cannot be repopulated.

<!-- image -->

## See also:

- A2.1.5 Realm lifecycle
- Chapter A5 Realm memory management
- B4.3.2 RMI\_DATA\_CREATE\_UNKNOWN command
- B4.3.5 RMI\_GRANULE\_DELEGATE command

## D1.5.2 NS memory flow

The following diagram describes how NS memory can be mapped into a Realm.

<!-- image -->

## See also:

- Chapter A5 Realm memory management
- B4.3.19 RMI\_RTT\_MAP\_UNPROTECTED command

- B4.3.22 RMI\_RTT\_UNMAP\_UNPROTECTED command

## D1.5.3 RIPAS change flow

The following diagram describes how a Realm requests a RIPAS change, and how that request is handled by the Host.

- The Realm calls RSI\_IPA\_STATE\_SET to request a RIPAS change for IPA range [base, top) .
- This causes a REC exit due to RIPAS change pending.

On taking a REC exit due to RIPAS change pending, the Host does the following:

- Reads the region base and top addresses from the RmiRecExit object.
- Applies the requested RIPAS change to an IPA range starting from the base of the target region, and extending no further than the top of the target region.
- Calls RMI\_REC\_ENTER to re-enter the REC.

The Realm observes in X1 the top of the region for which the RIPAS change was applied.

<!-- image -->

## See also:

- A5.4 RIPAS change
- B4.3.14 RMI\_REC\_ENTER command
- B4.3.21 RMI\_RTT\_SET\_RIPAS command
- B5.3.6 RSI\_IPA\_STATE\_SET command
- D2.2 Realm shared memory protocol flow