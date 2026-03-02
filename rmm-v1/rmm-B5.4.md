## B5.4 RSI types

This section defines types which are used in the RSI interface.

## B5.4.1 RsiCommandReturnCode type

The RsiCommandReturnCode enumeration represents a return code from an RSI command.

The RsiCommandReturnCode enumeration is a concrete type.

The width of the RsiCommandReturnCode enumeration is 64 bits.

See also:

- Chapter B1 Commands

The values of the RsiCommandReturnCode enumeration are shown in the following table.

|   Encoding | Name              | Description                                                                                    |
|------------|-------------------|------------------------------------------------------------------------------------------------|
|          0 | RSI_SUCCESS       | Command completed successfully                                                                 |
|          1 | RSI_ERROR_INPUT   | The value of a command input value caused the command to fail                                  |
|          2 | RSI_ERROR_STATE   | The state of the current Realm or current REC does not match the state expected by the command |
|          3 | RSI_INCOMPLETE    | The operation requested by the command is not complete                                         |
|          4 | RSI_ERROR_UNKNOWN | The operation requested by the command failed for an unknown reason                            |

Unused encodings for the RsiCommandReturnCode enumeration are reserved for use by future versions of this specification.

## B5.4.2 RsiHashAlgorithm type

The RsiHashAlgorithm enumeration represents hash algorithm.

The RsiHashAlgorithm enumeration is a concrete type.

The width of the RsiHashAlgorithm enumeration is 8 bits.

See also:

- B5.3.9 RSI\_REALM\_CONFIG command

The values of the RsiHashAlgorithm enumeration are shown in the following table.

|   Encoding | Name             | Description                                |
|------------|------------------|--------------------------------------------|
|          0 | RSI_HASH_SHA_256 | SHA-256 ( Secure Hash Standard (SHS) [15]) |
|          1 | RSI_HASH_SHA_512 | SHA-512 ( Secure Hash Standard (SHS) [15]) |

Unused encodings for the RsiHashAlgorithm enumeration are reserved for use by future versions of this specification.

## B5.4.3 RsiHostCall type

The RsiHostCall structure contains data structure used to pass Host call arguments and return values.

The RsiHostCall structure is a concrete type.

The width of the RsiHostCall structure is 256 ( 0x100 ) bytes.

See also:

- A4.5 Host call
- B5.3.4 RSI\_HOST\_CALL command

The members of the RsiHostCall structure are shown in the following table.

| Name     | Byte offset   | Type   | Description     |
|----------|---------------|--------|-----------------|
| imm      | 0x0           | UInt16 | Immediate value |
| gprs[0]  | 0x8           | Bits64 | Registers       |
| gprs[1]  | 0x10          | Bits64 | Registers       |
| gprs[2]  | 0x18          | Bits64 | Registers       |
| gprs[3]  | 0x20          | Bits64 | Registers       |
| gprs[4]  | 0x28          | Bits64 | Registers       |
| gprs[5]  | 0x30          | Bits64 | Registers       |
| gprs[6]  | 0x38          | Bits64 | Registers       |
| gprs[7]  | 0x40          | Bits64 | Registers       |
| gprs[8]  | 0x48          | Bits64 | Registers       |
| gprs[9]  | 0x50          | Bits64 | Registers       |
| gprs[10] | 0x58          | Bits64 | Registers       |
| gprs[11] | 0x60          | Bits64 | Registers       |
| gprs[12] | 0x68          | Bits64 | Registers       |
| gprs[13] | 0x70          | Bits64 | Registers       |
| gprs[14] | 0x78          | Bits64 | Registers       |
| gprs[15] | 0x80          | Bits64 | Registers       |
| gprs[16] | 0x88          | Bits64 | Registers       |
| gprs[17] | 0x90          | Bits64 | Registers       |
| gprs[18] | 0x98          | Bits64 | Registers       |
| gprs[19] | 0xa0          | Bits64 | Registers       |
| gprs[20] | 0xa8          | Bits64 | Registers       |
| gprs[21] | 0xb0          | Bits64 | Registers       |
| gprs[22] | 0xb8          | Bits64 | Registers       |
| gprs[23] | 0xc0          | Bits64 | Registers       |
| gprs[24] | 0xc8          | Bits64 | Registers       |
| gprs[25] | 0xd0          | Bits64 | Registers       |

| Name     | Byte offset   | Type   | Description   |
|----------|---------------|--------|---------------|
| gprs[26] | 0xd8          | Bits64 | Registers     |
| gprs[27] | 0xe0          | Bits64 | Registers     |
| gprs[28] | 0xe8          | Bits64 | Registers     |
| gprs[29] | 0xf0          | Bits64 | Registers     |
| gprs[30] | 0xf8          | Bits64 | Registers     |

Unused bits of the RsiHostCall structure SBZ.

## B5.4.4 RsiInterfaceVersion type

The RsiInterfaceVersion fieldset contains an RSI interface version.

The RsiInterfaceVersion fieldset is a concrete type.

The width of the RsiInterfaceVersion fieldset is 64 bits.

See also:

- B5.1 RSI version
- B5.3.10 RSI\_VERSION command

The fields of the RsiInterfaceVersion fieldset are shown in the following diagram.

<!-- image -->

The fields of the RsiInterfaceVersion fieldset are shown in the following table.

| Name   | Bits   | Description                                                            | Value   |
|--------|--------|------------------------------------------------------------------------|---------|
| minor  | 15:0   | Interface minor version number (the value y in interface version x.y ) | UInt16  |
| major  | 30:16  | Interface major version number (the value x in interface version x.y ) | UInt15  |
|        | 63:31  | Reserved                                                               | SBZ     |

## B5.4.5 RsiRealmConfig type

The RsiRealmConfig structure contains realm configuration.

The RsiRealmConfig structure is a concrete type.

The width of the RsiRealmConfig structure is 4096 ( 0x1000 ) bytes.

See also:

- B5.3.9 RSI\_REALM\_CONFIG command

The members of the RsiRealmConfig structure are shown in the following table.

| Name      | Byte offset   | Type             | Description                 |
|-----------|---------------|------------------|-----------------------------|
| ipa_width | 0x0           | UInt64           | IPA width in bits           |
| hash_algo | 0x8           | RsiHashAlgorithm | Hash algorithm              |
| rpv       | 0x200         | Bits512          | Realm Personalization Value |

Unused bits of the RsiRealmConfig structure MBZ.

## B5.4.6 RsiResponse type

The RsiResponse enumeration represents whether the Host accepted or rejected a Realm request.

The RsiResponse enumeration is a concrete type.

The width of the RsiResponse enumeration is 1 bits.

The values of the RsiResponse enumeration are shown in the following table.

|   Encoding | Name       | Description                      |
|------------|------------|----------------------------------|
|          0 | RSI_ACCEPT | Host accepted the Realm request. |
|          1 | RSI_REJECT | Host rejected the Realm request. |

## B5.4.7 RsiRipas type

The RsiRipas enumeration represents realm IPA state.

The RsiRipas enumeration is a concrete type.

The width of the RsiRipas enumeration is 8 bits.

See also:

- A5.4 RIPAS change
- B5.3.5 RSI\_IPA\_STATE\_GET command
- B5.3.6 RSI\_IPA\_STATE\_SET command

The values of the RsiRipas enumeration are shown in the following table.

|   Encoding | Name          | Description                                                                    |
|------------|---------------|--------------------------------------------------------------------------------|
|          0 | RSI_EMPTY     | Address where no Realm resources are mapped.                                   |
|          1 | RSI_RAM       | Address where private code or data owned by the Realm is mapped.               |
|          2 | RSI_DESTROYED | Address which is inaccessible to the Realm due to an action taken by the Host. |
|          3 | RSI_DEV       | Address where memory of an assigned Realm device is mapped.                    |

Unused encodings for the RsiRipas enumeration are reserved for use by future versions of this specification.

## B5.4.8 RsiRipasChangeDestroyed type

The RsiRipasChangeDestroyed enumeration represents whether a RIPAS change from DESTROYED should be permitted.

The RsiRipasChangeDestroyed enumeration is a concrete type.

The width of the RsiRipasChangeDestroyed enumeration is 1 bits.

The values of the RsiRipasChangeDestroyed enumeration are shown in the following table.

|   Encoding | Name                    | Description                                            |
|------------|-------------------------|--------------------------------------------------------|
|          0 | RSI_NO_CHANGE_DESTROYED | A RIPAS change from DESTROYED should not be permitted. |
|          1 | RSI_CHANGE_DESTROYED    | A RIPAS change from DESTROYED should be permitted.     |

## B5.4.9 RsiRipasChangeFlags type

The RsiRipasChangeFlags fieldset contains flags provided by the Realm when requesting a RIPAS change.

The RsiRipasChangeFlags fieldset is a concrete type.

The width of the RsiRipasChangeFlags fieldset is 64 bits.

The fields of the RsiRipasChangeFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RsiRipasChangeFlags fieldset are shown in the following table.

| Name      | Bits   | Description                                               | Value                   |
|-----------|--------|-----------------------------------------------------------|-------------------------|
| destroyed | 0:0    | Whether a RIPAS change from DESTROYED should be permitted | RsiRipasChangeDestroyed |
|           | 63:1   | Reserved                                                  | SBZ                     |