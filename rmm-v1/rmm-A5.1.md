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

- A2.1.3 Realm attributes
- A3.1.2 Realm LPA2 and IPA width

## A5.2.2 Realm IPA state

- A Protected IPA has an associated Realm IPA state (RIPAS).

The RIPAS values are shown in the following table.

| Name      | Description                                                                    |
|-----------|--------------------------------------------------------------------------------|
| DESTROYED | Address which is inaccessible to the Realm due to an action taken by the Host. |
| DEV       | Address where memory of an assigned Realm device is mapped.                    |
| EMPTY     | Address where no Realm resources are mapped.                                   |
| RAM       | Address where private code or data owned by the Realm is mapped.               |

RIPAS values are stored in an RTT.