## B5.3.8 RSI\_MEASUREMENT\_READ command

Read measurement for the current Realm.

See also:

- A7.1 Realm measurements
- D1.2.1 Realm creation flow

## B5.3.8.1 Interface

## B5.3.8.1.1 Input values

| Name   | Register   | Bits   | Type   | Description           |
|--------|------------|--------|--------|-----------------------|
| fid    | X0         | 63:0   | UInt64 | FID, value 0xC4000192 |
| index  | X1         | 63:0   | UInt64 | Measurement index     |

index 0 selects the RIM. An index of 1 or greater selects the corresponding REM.

## B5.3.8.1.2 Output values

| Name    | Register   | Bits   | Type                 | Description                                                 |
|---------|------------|--------|----------------------|-------------------------------------------------------------|
| result  | X0         | 63:0   | RsiCommandReturnCode | Command return status                                       |
| value_0 | X1         | 63:0   | Bits64               | Doubleword 0 of the Realm measurement identified by 'index' |
| value_1 | X2         | 63:0   | Bits64               | Doubleword 1 of the Realm measurement identified by 'index' |
| value_2 | X3         | 63:0   | Bits64               | Doubleword 2 of the Realm measurement identified by 'index' |
| value_3 | X4         | 63:0   | Bits64               | Doubleword 3 of the Realm measurement identified by 'index' |
| value_4 | X5         | 63:0   | Bits64               | Doubleword 4 of the Realm measurement identified by 'index' |
| value_5 | X6         | 63:0   | Bits64               | Doubleword 5 of the Realm measurement identified by 'index' |
| value_6 | X7         | 63:0   | Bits64               | Doubleword 6 of the Realm measurement identified by 'index' |
| value_7 | X8         | 63:0   | Bits64               | Doubleword 7 of the Realm measurement identified by 'index' |

If the size of the measurement value is smaller than 512 bits, the output values are padded with zeroes.

## B5.3.8.2 Failure conditions

ID

## Condition

index\_bound

pre:

index &gt; 4

post:

result

==

RSI\_ERROR\_INPUT

## B5.3.8.3 Success conditions

The RSI\_MEASUREMENT\_READ command does not have any success conditions.

## B5.3.8.4 Footprint

The RSI\_MEASUREMENT\_READ command does not have any footprint.