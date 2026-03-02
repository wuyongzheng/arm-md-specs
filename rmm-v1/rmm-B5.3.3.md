## B5.3.3 RSI\_FEATURES command

Read feature register.

In the current version of the interface, this command returns zero regardless of the index provided.

See also:

- A3.1 Realm feature discovery and selection

## B5.3.3.1 Interface

## B5.3.3.1.1 Input values

| Name   | Register   | Bits   | Type   | Description            |
|--------|------------|--------|--------|------------------------|
| fid    | X0         | 63:0   | UInt64 | FID, value 0xC4000191  |
| index  | X1         | 63:0   | UInt64 | Feature register index |

## B5.3.3.1.2 Output values

| Name   | Register   | Bits   | Type                 | Description            |
|--------|------------|--------|----------------------|------------------------|
| result | X0         | 63:0   | RsiCommandReturnCode | Command return status  |
| value  | X1         | 63:0   | Bits64               | Feature register value |

## B5.3.3.2 Failure conditions

The RSI\_FEATURES command does not have any failure conditions.

## B5.3.3.3 Success conditions

| ID    | Condition        |
|-------|------------------|
| index | value == Zeros() |

## B5.3.3.4 Footprint

The RSI\_FEATURES command does not have any footprint.