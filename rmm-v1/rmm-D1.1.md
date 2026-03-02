## D1.1 Granule delegation flows

## D1.1.1 Granule delegation flow

The following diagram shows how the GPT entry of a Granule is changed from GPT\_NS to GPT\_REALM.

See Arm Architecture Reference Manual Supplement, The Realm Management Extension (RME), for Armv9-A [2] for example software flows for the operations performed by the Monitor in this flow.

It is anticipated that the Monitor software will be required to use synchronization mechanisms to serialize access to the GPT.

<!-- image -->

## See also:

- A2.2.1 Granule attributes
- B4.3.5 RMI\_GRANULE\_DELEGATE command
- D1.1.2 Granule undelegation flow

## D1.1.2 Granule undelegation flow

The following diagram shows how the GPT entry of a Granule is changed from GPT\_REALM to GPT\_NS.

See Arm Architecture Reference Manual Supplement, The Realm Management Extension (RME), for Armv9-A [2] for example software flows for the operations performed by the Monitor in this flow.

It is anticipated that the Monitor software will be required to use synchronization mechanisms to serialize access to the GPT.

## See also:

- A2.2.1 Granule attributes
- B4.3.6 RMI\_GRANULE\_UNDELEGATE command
- D1.1.1 Granule delegation flow

<!-- image -->