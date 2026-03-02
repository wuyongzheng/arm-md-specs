## B5.4.4 RSI\_FEATURES command

Read feature register.

The following table indicates which feature register is returned depending on the index provided.

|   Index | Feature register       |
|---------|------------------------|
|       0 | RSI feature register 0 |

See also:

- Chapter A3 Feature discovery and configuration

## B5.4.4.1 Interface

## B5.4.4.1.1 Input values

| Name   | Register   | Bits   | Type   | Description            |
|--------|------------|--------|--------|------------------------|
| fid    | X0         | 63:0   | UInt64 | FID, value 0xC4000191  |
| index  | X1         | 63:0   | UInt64 | Feature register index |

## B5.4.4.1.2 Context

The RSI\_FEATURES command operates on the following context.

| Name   | Type     | Value Before         | Description   |
|--------|----------|----------------------|---------------|
| realm  | RmmRealm | CurrentRealm() false | Current Realm |

## B5.4.4.1.3 Output values

DRAFT

| Name   | Register   | Bits   | Type                 | Description            |
|--------|------------|--------|----------------------|------------------------|
| result | X0         | 63:0   | RsiCommandReturnCode | Command result         |
| value  | X1         | 63:0   | Bits64               | Feature register value |

## B5.4.4.2 Failure conditions

The RSI\_FEATURES command does not have any failure conditions.

## B5.4.4.3 Success conditions

| ID    | Condition                                             |
|-------|-------------------------------------------------------|
| value | post: value == RsiFeatureRegisterEncode(realm, index) |

## B5.4.4.4 Footprint

The RSI\_FEATURES command does not have any footprint.