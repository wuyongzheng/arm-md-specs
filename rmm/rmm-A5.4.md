## A5.4 RIPAS change

- DBTSQY A RIPAS change is a process via which the RIPAS of a region of Protected IPA space is changed, for a Realm whose state is REALM\_ACTIVE.
- IKXXBV A RIPAS change consists of actions taken by first the Realm, and then the Host:
- The Realm issues a RIPAS change request by executing RSI\_IPA\_STATE\_SET.
- -The input values to this command include:
* The requested IPA range: [base, top)
* The requested RIPAS value (either EMPTY or RAM)
* A flag which indicates whether a change from DESTROYED should be permitted
- -The RMM records these values in the REC, and then performs a REC exit due to RIPAS change pending.
- In response, the Host executes zero or more RMI\_RTT\_SET\_RIPAS commands.
- If the requested RIPAS value was RAM, at the next RMI\_REC\_ENTER the Host can optionally indicate that it rejects the RIPAS change request.

Output values from RSI\_IPA\_STATE\_SET indicate:

- The top of the IPA range which has been modified by the command ( new\_base ).
- If the requested RIPAS value was RAM, whether the Host rejected the Realm request.

Output values from RSI\_IPA\_STATE\_SET are expected to be handled by the Realm as follows:

SCTTQV

| new_base              | response   | Meaning                                                                                                              | Expected Realm action                                                                  |
|-----------------------|------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| new_base == base      | RSI_ACCEPT | RIPAS change incomplete.                                                                                             | Call RSI_IPA_STATE_SET again, with base = new_base .                                   |
| base < new_base < top | RSI_ACCEPT | RIPAS change incomplete.                                                                                             | Call RSI_IPA_STATE_SET again, with base = new_base .                                   |
| new_base == top       | RSI_ACCEPT | RIPAS change complete.                                                                                               | No further Realm action required.                                                      |
| new_base == base      | RSI_REJECT | RIPAS change request rejected.                                                                                       | Depends on protocol agreed between Realm and Host, out of scope of this specification. |
| base < new_base < top | RSI_REJECT | RIPAS change to partial region [base, new_base) . Host rejected request to change RIPAS for region [new_base, top) . | Depends on protocol agreed between Realm and Host, out of scope of this specification. |

IRFVTG

The RIPAS change process, together with the Realm Initial Measurement ensures that a Realm can always reliably determine the RIPAS of any Protected IPA.

ILPZWK

A RIPAS change is applied by one or more calls to the RMI\_RTT\_SET\_RIPAS command.

IMMHMZ

Successful execution of RMI\_RTT\_SET\_RIPAS targets an RTTE at address rec.ripas\_addr .

- IJHJGZ On successful execution of RMI\_RTT\_SET\_RIPAS, both of the following are set to the address of the next page

whose RIPAS is to be modified:

- rec.ripas\_addr
- The command output value

IGXDDX

If both of the following are true on successful execution of RMI\_RTT\_SET\_RIPAS

- The RIPAS change request indicated that a change from DESTROYED should not be permitted
- A page P within the target IPA range has RIPAS value DESTROYED

then rec.ripas\_addr and the command output value are both set to P .

- IHXKPB On REC entry following a REC exit due to RIPAS change, GPR values are updated to indicate for how much of the target IPA range the RIPAS change has been applied.
- STZYZV To complete a RIPAS change for a given target IPA range, a Realm should execute RSI\_IPA\_STATE\_SET in a loop, until the value of X1 reaches the top of the target IPA range.
- RLDMLC On REC entry following a REC exit due to RIPAS change, rec.ripas\_response is set to the value of enter.flags.ripas\_response .
- IDRPPK If all of the following are true then the output value of RSI\_IPA\_STATE\_SET indicates 'Host rejected the request':
- rec.ripas\_value is RAM.
- rec.ripas\_addr is not equal to rec.ripas\_top .
- rec.ripas\_response is REJECT.

Otherwise, the output value of RSI\_IPA\_STATE\_SET indicates 'Host accepted the request'.

SBZWWC Receipt of a rejection for a RIPAS change request whose parameters were valid is expected to be fatal for the Realm.

See also:

- A2.3.2 REC attributes
- A4.2 REC entry
- A4.3.8 REC exit due to RIPAS change pending
- A5.2.2 Realm IPA state
- A7.1.1 Realm Initial Measurement
- B3.40 RecRipasChangeResponse function
- B4.3.14 RMI\_REC\_ENTER command
- B4.3.21 RMI\_RTT\_SET\_RIPAS command
- B5.3.6 RSI\_IPA\_STATE\_SET command
- D1.5.3 RIPAS change flow