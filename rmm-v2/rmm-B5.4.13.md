## B5.4.13 RSI\_PLANE\_ENTER command

Enter a Plane.

See also:

- [A5.2.4 RSI command access to a Protected IPA](rmm-A5.1.md#a524-rsi-command-access-to-a-protected-ipa)
- [A10.2 Planes exception model](rmm-A10.2.md)

## B5.4.13.1 Interface

## B5.4.13.1.1 Input values

| Name      | Register   | Bits   | Type    | Description            |
|-----------|------------|--------|---------|------------------------|
| fid       | X0         | 63:0   | UInt64  | FID, value 0xC40001A3  |
| plane_idx | X1         | 63:0   | UInt64  | Index of target Plane  |
| run_ptr   | X2         | 63:0   | Address | IPA of PlaneRun object |

## B5.4.13.1.2 Context

The RSI\_PLANE\_ENTER command operates on the following context.

| Name   | Type                      | Value Before         | Description     |
|--------|---------------------------|----------------------|-----------------|
| realm  | RmmRealm CurrentRealm()   | false                | Current Realm   |
| run    | RsiPlaneRun               | RsiPlaneRunAt( false | PlaneRun object |
| walk   | RmmRttWalkResult RttWalk( | false                | RTT walk result |


## B5.4.13.1.3 Output values

| Name   | Register   | Bits   | Type                 | Description    |
|--------|------------|--------|----------------------|----------------|
| result | X0         | 63:0   | RsiCommandReturnCode | Command result |

## B5.4.13.2 Failure conditions

* idx_bound
  * pre: (plane_idx == 0 || plane_idx > realm.num_aux_planes)
  * post: result == RSI_ERROR_INPUT
* run_align
  * pre: !AddrIsRsiGranuleAligned(run_ptr)
  * post: result == RSI_ERROR_INPUT
* run_bound
  * pre: !AddrIsProtected(run_ptr, realm)
  * post: result == RSI_ERROR_INPUT
* run_empty
  * pre: walk.rtte.ripas == RIPAS_EMPTY
  * post: result == RSI_ERROR_INPUT
* el
  * pre: run.enter.pstate[3] == '1'
  * post: result == RSI_ERROR_INPUT

## B5.4.13.2.1 Failure condition ordering

The RSI\_PLANE\_ENTER command does not have any failure condition orderings.

## B5.4.13.3 Success conditions

* plane_exit
  * post: run.exit contains Plane exit syndrome information.

## B5.4.13.4 Footprint

The RSI\_PLANE\_ENTER command does not have any footprint.

