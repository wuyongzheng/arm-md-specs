## A5.4 RIPAS change

- DBTSQY A RIPAS change is a process via which the RIPAS of a region of Protected IPA space is changed, for a Realm whose state is REALM\_ACTIVE.
- IKXXBV

A RIPAS change consists of actions taken first by the Realm, and then by the Host:

- The Realm issues a RIPAS change request by executing an RSI command.
- -The input values to the RSI command include the requested IPA range: [base, top) .
- -The target RIPAS value is either passed as an input, or is implied by the command.
- -The RMM records the request the REC, and then performs a REC exit.
- In response, the Host executes zero or more RMI commands to apply the RIPAS change.
- If the requested RIPAS value was not RIPAS\_EMPTY then at the next RMI\_REC\_ENTER the Host can optionally indicate that it rejects the RIPAS change request.

Output values from the RSI command indicate:

- The top of the IPA range which has been modified by the command ( new\_base ).
- Whether the Host accepted or rejected the Realm request.

## See also:

- A5.2.2 Realm IPA state

## A5.4.1 Realm view of RIPAS change

- ICKBLH The RSI commands which can initiate a RIPAS change request are:
- RSI\_IPA\_STATE\_SET
- -The target RIPAS value, either RIPAS\_EMPTY or RIPAS\_RAM, is provided as an input value.
- -If the target RIPAS value is RIPAS\_RAM, a flag indicates whether a change from RIPAS\_DESTROYED should be permitted.
- RSI\_VDEV\_VALIDATE\_MAPPING
- -The target RIPAS value is RIPAS\_DEV.
- IHXKPB On REC entry following a REC exit due to a RIPAS change request, GPR values are updated to indicate for how much of the target IPA range the RIPAS change has been applied.

DRAFT

- STZYZV To complete a RIPAS change for a given target IPA range, a Realm should execute the initiating command in a loop, until the value of X1 reaches the top of the target IPA range.
- SBZWWC Receipt of a rejection for a RIPAS change request whose parameters were valid is expected to be fatal for the Realm.
- SCTTQV Output values from the initiating RSI command are expected to be handled by the Realm as follows:

| new_base              | response            | Meaning                        | Expected Realm action                                                                  |
|-----------------------|---------------------|--------------------------------|----------------------------------------------------------------------------------------|
| new_base == base      | RSI_RESPONSE_ACCEPT | RIPAS change incomplete.       | Call the command again, with base = new_base .                                         |
| base < new_base < top | RSI_RESPONSE_ACCEPT | RIPAS change incomplete.       | Call the command again, with base = new_base .                                         |
| new_base == top       | RSI_RESPONSE_ACCEPT | RIPAS change complete.         | No further Realm action required.                                                      |
| new_base == base      | RSI_RESPONSE_REJECT | RIPAS change request rejected. | Depends on protocol agreed between Realm and Host, out of scope of this specification. |

| new_base        | response            | Meaning                                                                                                              | Expected Realm action                                                                  |
|-----------------|---------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| base < new_base | RSI_RESPONSE_REJECT | RIPAS change to partial region [base, new_base) . Host rejected request to change RIPAS for region [new_base, top) . | Depends on protocol agreed between Realm and Host, out of scope of this specification. |

IRFVTG

The RIPAS change process, together with the Realm Initial Measurement ensures that a Realm can always reliably determine the RIPAS of any Protected IPA.

## See also:

- A7.1.1 Realm Initial Measurement
- B5.4.7 RSI\_IPA\_STATE\_SET command
- B5.4.21 RSI\_VDEV\_VALIDATE\_MAPPING command

## A5.4.2 Host view of RIPAS change to RIPAS\_EMPTY or RIPAS\_RAM

- IWBCJL A RIPAS change request whose target is RIPAS\_EMPTY or RIPAS\_RAM results in a REC exit due to RIPAS change.
- ILPZWK A RIPAS change whose target is RIPAS\_EMPTY or RIPAS\_RAM is applied by one or more calls to the RMI\_RTT\_SET\_RIPAS command.
- IMMHMZ Successful execution of RMI\_RTT\_SET\_RIPAS targets an RTTE at address rec.ripas\_addr .
- IJHJGZ On successful execution of RMI\_RTT\_SET\_RIPAS, both of the following are set to the address of the next page whose RIPAS is to be modified:
- rec.ripas\_addr
- The command output value
- IGXDDX If all of the following are true on successful execution of RMI\_RTT\_SET\_RIPAS

DRAFT

- The target RIPAS is RIPAS\_RAM
- The RIPAS change request indicated that a change from RIPAS\_DESTROYED to RIPAS\_RAM should not be permitted
- A page P within the target IPA range has RIPAS value RIPAS\_DESTROYED

then rec.ripas\_addr and the command output value are both set to P .

- RLDMLC On REC entry following a REC exit due to RIPAS change, rec.ripas\_response is set to the value of enter.flags.ripas\_response .
- IDRPPK If all of the following are true then the output value of RSI\_IPA\_STATE\_SET indicates 'Host rejected the request':
- rec.ripas\_value is RIPAS\_RAM.
- rec.ripas\_addr is not equal to rec.ripas\_top .
- rec.ripas\_response is REJECT.

Otherwise, the output value of RSI\_IPA\_STATE\_SET indicates 'Host accepted the request'.

## See also:

- A4.3.8 REC exit due to RIPAS change pending
- B4.5.51 RMI\_REC\_ENTER command
- B4.5.75 RMI\_RTT\_SET\_RIPAS command
- D1.5.3 RIPAS change flow

## A5.4.3 Host view of RIPAS change to RIPAS\_DEV

- ITLZWR A RIPAS change request whose target is RIPAS\_DEV results in a REC exit due to VDEV mapping validation.
- IBJBJB A RIPAS change whose target is RIPAS\_DEV is applied by one or more calls to the RMI\_RTT\_DEV\_VALIDATE command.

See also:

- A4.3.13 REC exit due to VDEV mapping validation
- A5.5 VDEV mapping validation
- A9.6.2 Realm validation of device memory mappings
- B4.5.51 RMI\_REC\_ENTER command
- B4.5.71 RMI\_RTT\_DEV\_VALIDATE command
- D1.5.3 RIPAS change flow

<!-- image -->