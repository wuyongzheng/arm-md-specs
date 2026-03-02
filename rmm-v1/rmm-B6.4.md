## B6.4 PSCI types

This section defines types which are used in the PSCI interface.

## B6.4.1 PsciInterfaceVersion type

The PsciInterfaceVersion fieldset contains an PSCI interface version.

The PsciInterfaceVersion fieldset is a concrete type.

The width of the PsciInterfaceVersion fieldset is 64 bits.

The fields of the PsciInterfaceVersion fieldset are shown in the following diagram.

<!-- image -->

| 63          |
|-------------|
| MBZ         |
| 15 16 30 31 |
| major MBZ   |

The fields of the PsciInterfaceVersion fieldset are shown in the following table.

| Name   | Bits   | Description                                                            | Value   |
|--------|--------|------------------------------------------------------------------------|---------|
| minor  | 15:0   | Interface minor version number (the value y in interface version x.y ) | UInt16  |
| major  | 30:16  | Interface major version number (the value x in interface version x.y ) | UInt15  |
|        | 63:31  | Reserved                                                               | MBZ     |

## B6.4.2 PsciReturnCode type

The PsciReturnCode enumeration represents the return code of a PSCI command.

The PsciReturnCode enumeration is a concrete type.

The width of the PsciReturnCode enumeration is 64 bits.

The values of the PsciReturnCode enumeration are shown in the following table.

|   Encoding | Name                    | Description                 |
|------------|-------------------------|-----------------------------|
|         -9 | PSCI_INVALID_ADDRESS    | Refer to PSCI specification |
|         -8 | PSCI_DISABLED           | Refer to PSCI specification |
|         -7 | PSCI_NOT_PRESENT        | Refer to PSCI specification |
|         -6 | PSCI_INTERNAL_FAILURE   | Refer to PSCI specification |
|         -5 | PSCI_ON_PENDING         | Refer to PSCI specification |
|         -4 | PSCI_ALREADY_ON         | Refer to PSCI specification |
|         -3 | PSCI_DENIED             | Refer to PSCI specification |
|         -2 | PSCI_INVALID_PARAMETERS | Refer to PSCI specification |
|         -1 | PSCI_NOT_SUPPORTED      | Refer to PSCI specification |

|   Encoding | Name         | Description                 |
|------------|--------------|-----------------------------|
|          0 | PSCI_SUCCESS | Refer to PSCI specification |
|          1 | PSCI_OFF     | Refer to PSCI specification |

Unused encodings for the PsciReturnCode enumeration are reserved for use by future versions of this specification.