## B5.4.17 RSI\_VDEV\_DMA\_DISABLE command

Disable DMA.

B5.4.17.1

Interface

B5.4.17.1.1

Input values

| Name    | Register   | Bits   | Type   | Description             |
|---------|------------|--------|--------|-------------------------|
| fid     | X0         | 63:0   | UInt64 | FID, value 0xC40001A4   |
| vdev_id | X1         | 63:0   | Bits64 | Realm device identifier |

## B5.4.17.1.2 Context

The RSI\_VDEV\_DMA\_DISABLE command operates on the following context.

| Name   | Type     | Value                           | Before   | Description   |
|--------|----------|---------------------------------|----------|---------------|
| realm  | RmmRealm | CurrentRealm()                  | false    | Current Realm |
| vdev   | RmmVdev  | VdevFromVdevId( realm, vdev_id) | false    | Realm device  |

## B5.4.17.1.3 Output values

| Name   | Register   | Bits   | Type                 | Description    |
|--------|------------|--------|----------------------|----------------|
| result | X0         | 63:0   | RsiCommandReturnCode | Command result |


## B5.4.17.2 Failure conditions

* da_en
  * pre: realm.feat_da != FEATURE_TRUE
  * post: result == RSI_ERROR_STATE
* vdev_id
  * pre: VdevIdIsFree(realm, vdev_id)
  * post: result == RSI_ERROR_INPUT

## B5.4.17.2.1 Failure condition ordering

| [da_en] < [vdev_id]   |
|-----------------------|

## B5.4.17.3 Success conditions

* dma_state
  * post: vdev.dma_state == VDEV_DMA_DISABLED

## B5.4.17.4 Footprint

The RSI\_VDEV\_DMA\_DISABLE command does not have any footprint.


<!-- image -->