## B4.5.14 RMI\_FEATURES command

Read feature register.

The following table indicates which feature register is returned depending on the index provided.

|   Index | Feature register       |
|---------|------------------------|
|       0 | RMI feature register 0 |
|       1 | RMI feature register 1 |
|       2 | RMI feature register 2 |
|       3 | RMI feature register 3 |
|       4 | RMI feature register 4 |

## See also:

- Chapter A3 Feature discovery and configuration

## B4.5.14.1 Interface

## B4.5.14.1.1 Input values

| Name   | Register   | Bits   | Type   | Description            |
|--------|------------|--------|--------|------------------------|
| fid    | X0         | 63:0   | UInt64 | FID, value 0xC4000165  |
| index  | X1         | 63:0   | UInt64 | Feature register index |

## B4.5.14.1.2 Output values

| Name   | Register   | Bits   | Type      | Description            |
|--------|------------|--------|-----------|------------------------|
| result | X0         | 63:0   | RmiResult | Command result         |
| value  | X1         | 63:0   | Bits64    | Feature register value |


## B4.5.14.2 Failure conditions

The RMI\_FEATURES command does not have any failure conditions.

## B4.5.14.3 Success conditions

| ID    | Condition                                      |
|-------|------------------------------------------------|
| value | post: value == RmiFeatureRegisterEncode(index) |

## B4.5.14.4 Footprint

The RMI\_FEATURES command does not have any footprint.