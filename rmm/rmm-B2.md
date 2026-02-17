## Chapter B2 Interface versioning

This section describes how the RMI and RSI interfaces are versioned, and how the caller of each can determine whether there exists a mutually acceptable revision of the interface via which it can communicate with the RMM.

Other interfaces exposed by the RMM, such as PSCI, may define their own versioning schemes which differ from that used by RMI and RSI. For details, refer to the specification of the interface concerned.

ILZVQR

Revisions of the RMI and the RSI are identified by a (major, minor) version tuple.

The semantics of this version tuple are as follows. For two revisions of the interface P = (majP, minP) and Q = (majQ, minQ) :

- If majP != majQ then the two interfaces may contain incompatible commands.
- If majP == majQ and minP &lt; minQ then:
- -Every command defined in P has the same behavior in Q, when called with input values that are specified as valid in P.
- -A command defined in P may accept additional input values in Q. These could be provided via any of:
* Input registers which were unused in P.
* Input memory locations which were specified as SBZ in P.
* Encodings which were specified as reserved in P.
- -A command defined in P may return additional output values in Q. These could be returned via any of:
* Output registers which were unused in P.
* Output memory locations which were specified as MBZ in P.
* Encodings which were specified as reserved in P.
- -Q may contain additional commands which are not present in P.
- P is less than Q if one of the following conditions is true:
- -majP &lt; majQ -majP == majQ and minP &lt; minQ

IZCPBC For each interface, an RMM implementation supports a set of revisions. The size of this set is at least one.

- IRMSLZ If an RMM implementation supports a given interface revision (x, y) then Arm expects that it will also supports all earlier revisons with the same major version number. That is:

<!-- formula-not-decoded -->

Apossible exception to this may occur if a security vulnerability is discovered in a particular revision of the interface. For example, if interface revision (x, bad) is found to contain a vulnerability then an RMM implementation may choose to support the following set of revisions:

<!-- formula-not-decoded -->

- IGLDQG The set of interface revisions supported by an RMM implementation may include revisons with different major version numbers, for example:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

- IJNVXJ The RMI\_VERSION and RSI\_VERSION commands allow the caller and the RMM to determine whether there exists a mutually acceptable revision of the interface via which the two components can communicate.

In each case:

- The caller provides a requested interface revision.
- The output values include a status code and two revisions which are supported by the RMM: a lower revision and a higher revision .
- The higher revision value is the highest interface revision which is supported by the RMM.
- The lower revision is less than or equal to the higher revision .

The status code and lower revision output values indicate which of the following is true, in order of precedence:

- a) The RMM supports an interface revision which is compatible with the requested revision.
- The status code is 'success'.

- The lower revision is equal to the requested revision.
- b) The RMM does not support an interface revision which is compatible with the requested revision The RMM supports an interface revision which is incompatible with and less than the requested revision.
- The status code is 'failure'.
- The lower revision is the highest interface revision which is both less than the requested revision and supported by the RMM.
- c) The RMM does not support an interface revision which is compatible with the requested revision The RMM supports an interface revision which is incompatible with and greater than the requested revision.
- The status code is 'failure'.
- The lower revision is equal to the higher revision .

The following table shows how each of a set of example scenarios maps onto the above outcomes.

|   Scenario | Revisions supported by RMM   | Revision requested by caller   | Outcome       | 'Lower revision' output value   | 'Higher revision' output value   |
|------------|------------------------------|--------------------------------|---------------|---------------------------------|----------------------------------|
|          1 | (1, 0)                       | (1, 0)                         | Success ( a ) | (1, 0)                          | (1, 0)                           |
|          2 | (1, 0) , (1, 1)              | (1, 0)                         | Success ( a ) | (1, 0)                          | (1, 1)                           |
|          3 | (1, 0) , (2, 0)              | (1, 0)                         | Success ( a ) | (1, 0)                          | (2, 0)                           |
|          4 | (1, 0)                       | (1, 1)                         | Failure ( b ) | (1, 0)                          | (1, 0)                           |
|          5 | (1, 0) , (1, 1)              | (1, 2)                         | Failure ( b ) | (1, 1)                          | (1, 1)                           |
|          6 | (1, 0) , (1, 1)              | (2, 0)                         | Failure ( b ) | (1, 1)                          | (1, 1)                           |
|          7 | (1, 0) , (1, 1) , (1, 3)     | (1, 2)                         | Failure ( b ) | (1, 1)                          | (1, 3)                           |
|          8 | (1, 0)                       | (2, 0)                         | Failure ( b ) | (1, 0)                          | (1, 0)                           |
|          9 | (1, 0)                       | (2, 1)                         | Failure ( b ) | (1, 0)                          | (1, 0)                           |
|         10 | (1, 0) , (1, 1)              | (2, 0)                         | Failure ( b ) | (1, 1)                          | (1, 1)                           |
|         11 | (1, 0) , (1, 1)              | (2, 1)                         | Failure ( b ) | (1, 1)                          | (1, 1)                           |
|         12 | (1, 0) , (1, 1) , (2, 0)     | (2, 1)                         | Failure ( b ) | (2, 0)                          | (2, 0)                           |
|         13 | (2, 0)                       | (1, 0)                         | Failure ( c ) | (2, 0)                          | (2, 0)                           |
|         14 | (2, 0)                       | (1, 1)                         | Failure ( c ) | (2, 0)                          | (2, 0)                           |
|         15 | (2, 0) , (2, 1)              | (1, 0)                         | Failure ( c ) | (2, 1)                          | (2, 1)                           |

## See also:

- B4.1 RMI version
- B4.3.23 RMI\_VERSION command
- B5.1 RSI version
- B5.3.10 RSI\_VERSION command