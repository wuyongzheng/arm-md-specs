## B5.4.10 RSI\_MEM\_GET\_PERM\_VALUE command

Get overlay permission value for a specified (plane index, overlay permission index) tuple.

See also:

- A10.3.2 Stage 2 Access Permissions within a multi-Plane Realm

## B5.4.10.1 Interface

## B5.4.10.1.1 Input values

| Name        | Register   | Bits   | Type   | Description           |
|-------------|------------|--------|--------|-----------------------|
| fid         | X0         | 63:0   | UInt64 | FID, value 0xC40001A0 |
| plane_index | X1         | 63:0   | UInt64 | Plane index           |
| perm_index  | X2         | 63:0   | UInt64 | Permission index      |

## B5.4.10.1.2 Context

The RSI\_MEM\_GET\_PERM\_VALUE command operates on the following context.

| Name   | Type     | Value          | Before   | Description   |
|--------|----------|----------------|----------|---------------|
| realm  | RmmRealm | CurrentRealm() | false    | Current Realm |

## B5.4.10.1.3 Output values

| Name   | Register   | Bits   | Type                 | Description             |
|--------|------------|--------|----------------------|-------------------------|
| result | X0         | 63:0   | RsiCommandReturnCode | Command result          |
| value  | X1         | 63:0   | Bits64               | Memory permission value |

DRAFT

## B5.4.10.2 Failure conditions

## ID Condition

plane\_bound

pre:

plane\_index &gt; realm.num\_aux\_planes

post:

result == RSI\_ERROR\_INPUT

perm\_bound

pre:

perm\_index &gt;=

RMM\_NUM\_PERM\_OVERLAY\_INDICES

post:

result == RSI\_ERROR\_INPUT

## B5.4.10.2.1 Failure condition ordering

The RSI\_MEM\_GET\_PERM\_VALUE command does not have any failure condition orderings.

## B5.4.10.3 Success conditions

| ID    | Condition                                                              |
|-------|------------------------------------------------------------------------|
| label | post: value == realm.overlay_perms[[plane_index]].values[[perm_index]] |

## B5.4.10.4 Footprint

The RSI\_MEM\_GET\_PERM\_VALUE command does not have any footprint.

<!-- image -->