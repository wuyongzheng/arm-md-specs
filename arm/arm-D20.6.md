## D20.6 Virtual SError exceptions and delegated SError exceptions

ILSSCN

EL2 provides a virtual SError exception.

For more information, see:

- Virtual asynchronous exceptions

- Virtual exceptions when an implementation includes EL2.

IYLSLH

When FEAT\_E3DSE is implemented, EL3 provides delegated SError exceptions. For more information, see Delegated SErrors.

## IZXMPL FEAT\_RAS provides:

- Mechanisms to allow a hypervisor to specify the syndrome value reported to a guest Operating System on taking a virtual SError exception.
- Mechanisms to allow firmware to specify the syndrome value reported to a hypervisor or guest Operating System on taking a delegated SError exception.
- Support for EL0 or EL1 to isolate a virtual SError exception and for EL0, EL1, or EL2 to isolate a delegated SError exception as if it was a physical SError exception. See ESB and virtual SError exceptions.