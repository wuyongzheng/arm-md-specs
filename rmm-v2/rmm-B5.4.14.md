## B5.4.14 RSI\_PLANE\_SYSREG\_READ command

Read a Plane register.

See also:

- A10.2.6 Pn system registers

## B5.4.14.1 Interface

## B5.4.14.1.1 Input values

| Name      | Register   | Bits   | Type             | Description             |
|-----------|------------|--------|------------------|-------------------------|
| fid       | X0         | 63:0   | UInt64           | FID, value 0xC40001AE   |
| plane_idx | X1         | 63:0   | UInt64           | Index of target Plane   |
| addr      | X2         | 63:0   | RsiSysregAddress | System register address |

The encoding value is an architecturally-defined system register encoding.

See also:

- Arm Architecture Reference Manual for A-Profile architecture [3]

## B5.4.14.1.2 Context

The RSI\_PLANE\_SYSREG\_READ command operates on the following context.

| Name   | Type     | Value          | Before   | Description   |
|--------|----------|----------------|----------|---------------|
| realm  | RmmRealm | CurrentRealm() | false    | Current Realm |
| rec    | RmmRec   | CurrentRec()   | false    | Current REC   |

DRAFT

## B5.4.14.1.3 Output values

| Name       | Register   | Bits   | Type                 | Description                            |
|------------|------------|--------|----------------------|----------------------------------------|
| result     | X0         | 63:0   | RsiCommandReturnCode | Command result                         |
| value_low  | X1         | 63:0   | Bits64               | Lower 64 bits of system register value |
| value_high | X2         | 63:0   | Bits64               | Upper 64 bits of system register value |

## B5.4.14.2 Failure conditions

| ID           | Condition                                                                   |
|--------------|-----------------------------------------------------------------------------|
| idx_bound    | pre: plane_idx > realm.num_aux_planes post: result == RSI_ERROR_INPUT       |
| sysreg_valid | pre: !PlaneSysregValid(rec, addr, RMM_READ) post: result == RSI_ERROR_INPUT |

## B5.4.14.2.1 Failure condition ordering

The RSI\_PLANE\_SYSREG\_READ command does not have any failure condition orderings.

## B5.4.14.3 Success conditions

```
ID Condition value_64 pre: addr.d128 == RSI_FALSE post: (Zeros{64}() :: value_low) == PlaneSysregValue(rec, plane_idx, addr) value_128 pre: addr.d128 == RSI_TRUE post: (value_high :: value_low) == PlaneSysregValue(rec, plane_idx, addr)
```

## B5.4.14.4 Footprint

The RSI\_PLANE\_SYSREG\_READ command does not have any footprint.

<!-- image -->