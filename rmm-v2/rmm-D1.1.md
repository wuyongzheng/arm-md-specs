## D1.1 Granule delegation flows

## D1.1.1 Granule delegation flow

The following diagram shows how the GPT entry of a Granule is changed to GPT\_REALM.

See Arm Architecture Reference Manual Supplement, The Realm Management Extension (RME), for Armv9-A [2] for example software flows for the operations performed by the Monitor in this flow.

It is anticipated that the Monitor software will be required to use synchronization mechanisms to serialize access to the GPT.

<!-- image -->

See also:

- A2.3.6 Granule state
- B4.5.17 RMI\_GRANULE\_RANGE\_DELEGATE command
- D1.1.2 Granule undelegation flow

## D1.1.2 Granule undelegation flow

The following diagram shows how the GPT entry of a Granule is changed from GPT\_REALM.

See Arm Architecture Reference Manual Supplement, The Realm Management Extension (RME), for Armv9-A [2] for example software flows for the operations performed by the Monitor in this flow.

It is anticipated that the Monitor software will be required to use synchronization mechanisms to serialize access to the GPT.

Figure D1.1: Granule delegation flow

## See also:

- A2.3.6 Granule state
- B4.5.18 RMI\_GRANULE\_RANGE\_UNDELEGATE command
- D1.1.1 Granule delegation flow

Figure D1.2: Granule undelegation flow

<!-- image -->

