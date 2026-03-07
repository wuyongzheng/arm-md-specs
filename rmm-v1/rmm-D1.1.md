## D1.1 Granule delegation flows

## D1.1.1 Granule delegation flow

The following diagram shows how the GPT entry of a Granule is changed from GPT\_NS to GPT\_REALM.

See Arm Architecture Reference Manual Supplement, The Realm Management Extension (RME), for Armv9-A [2] for example software flows for the operations performed by the Monitor in this flow.

It is anticipated that the Monitor software will be required to use synchronization mechanisms to serialize access to the GPT.

<!-- image -->

## See also:

- [A2.2.1 Granule attributes](rmm-A2.2.md#a221-granule-attributes)
- [B4.3.5 RMI\_GRANULE\_DELEGATE command](rmm-B4.3.5.md)
- [D1.1.2 Granule undelegation flow](rmm-D1.1.md#d112-granule-undelegation-flow)

## D1.1.2 Granule undelegation flow

The following diagram shows how the GPT entry of a Granule is changed from GPT\_REALM to GPT\_NS.

See Arm Architecture Reference Manual Supplement, The Realm Management Extension (RME), for Armv9-A [2] for example software flows for the operations performed by the Monitor in this flow.

It is anticipated that the Monitor software will be required to use synchronization mechanisms to serialize access to the GPT.

## See also:

- [A2.2.1 Granule attributes](rmm-A2.2.md#a221-granule-attributes)
- [B4.3.6 RMI\_GRANULE\_UNDELEGATE command](rmm-B4.3.6.md)
- [D1.1.1 Granule delegation flow](rmm-D1.1.md#d111-granule-delegation-flow)

<!-- image -->