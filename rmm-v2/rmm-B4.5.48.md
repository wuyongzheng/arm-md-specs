## B4.5.48 RMI\_REALM\_TERMINATE command

Terminates a Realm.

The RMI\_REALM\_TERMINATE command may initiate a Stateful RMI Operation.

See also:

- A2.2 Realm
- B4.5.45 RMI\_REALM\_ACTIVATE command
- D1.2.5 Realm destruction flow

## B4.5.48.1 Interface

## B4.5.48.1.1 Input values

| Name   | Register   | Bits   | Type    | Description           |
|--------|------------|--------|---------|-----------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC4000201 |
| rd     | X1         | 63:0   | Address | PA of the RD          |

## B4.5.48.1.2 Context

The RMI\_REALM\_TERMINATE command operates on the following context.

| Name   | Type     | Value       | Before   | Description   |
|--------|----------|-------------|----------|---------------|
| realm  | RmmRealm | RealmAt(rd) | false    | Realm         |

## B4.5.48.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |


## B4.5.48.2 Failure conditions

| ID          | Condition                                                                  |
|-------------|----------------------------------------------------------------------------|
| rd_align    | pre: !AddrIsRmiGranuleAligned(rd) post: result.status == RMI_ERROR_INPUT   |
| rd_tracking | pre: !PaIsTrackedFine(rd) post: result.status == RMI_ERROR_INPUT           |
| rd_state    | pre: GranuleAt(rd).state != GRAN_RD post: result.status == RMI_ERROR_INPUT |
| rec_running | pre: AnyRecRunning(realm) post: result.status == RMI_ERROR_REALM           |

## B4.5.48.2.1 Failure condition ordering

[rd\_tracking, rd\_state] &lt; [rec\_running]

<!-- image -->

## B4.5.48.3 Success conditions

| ID          | Condition                          |
|-------------|------------------------------------|
| realm_state | post: realm.state == REALM_ZOMBIE  |
| result      | post: result.status == RMI_SUCCESS |

## B4.5.48.4 Footprint


| ID          | Value       |
|-------------|-------------|
| realm_state | realm.state |