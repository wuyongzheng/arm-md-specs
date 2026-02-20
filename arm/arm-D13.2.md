## D13.2 Accuracy of the Performance Monitors

The Performance Monitors:

- Are a non-invasive debug component. See Non-invasive behavior.
- Must provide broadly accurate and statistically useful count information.

## However, the Performance Monitors allow for:

- Areasonable degree of inaccuracy in the counts to keep the implementation and validation cost low. See A reasonable degree of inaccuracy.
- IMPLEMENTATION DEFINED controls, such as those in ACTLR registers, that software must configure before using certain PMU events. For example, to configure how the PE generates PMU events for components such as external caches and external memory.
- Other IMPLEMENTATION DEFINED controls, such as those in ACTLR registers, to optionally put the PE in an operating state that might do one or both of the following:
- -Change the level of non-invasiveness of the Performance Monitors so that enabling an event counter can impact the performance or behavior of the PE.
- -Allow inaccurate counts. This includes, but is not limited to, cycle counts.

## D13.2.1 Non-invasive behavior

The Performance Monitors are a non-invasive debug feature. A non-invasive debug feature permits the observation of data and program flow. Performance Monitors, PC Sample-based Profiling and Trace are non-invasive debug features.

Non-invasive debug components do not guarantee that they do not make any changes to the behavior or performance of the processor. Any changes that do occur must not be severe however, as this will reduce the usefulness of event counters for performance measurement and profiling. This does not include any change to program behavior that results from the same program being instrumented to use the Performance Monitors, or from some other performance monitoring process being run concurrently with the process being profiled in a multitasking operating system. As such, a reasonable variation in performance is permissible.

Note

Power consumption is one measure of performance. Therefore, a reasonable variation in power consumption is permissible.

Arm does not define a reasonable variation in performance , but recommends that such a variation is kept within 5% of normal operating performance, when averaged across a suite of code that is representative of the application workload.

Note

For profiles other than A-profile, there is the potential for stronger requirements. Ultimately, performance requirements are determined by end-users, and not set by the architecture.

For some common architectural events, this requirement to be non-invasive can conflict with the requirement to present an accurate value of the count under normal operating conditions. Should an implementation require more performance-invasive techniques to accurately count an event, there are the following options:

- If the event is optional, define an alternative IMPLEMENTATION DEFINED event that accurately counts the event and document the impact on performance of enabling the event.
- Provide an IMPLEMENTATION DEFINED control that disables accurate counting of the event to restore broadly accurate performance, and document the impact on performance of accurate counting.

When FEAT\_SEBEP is implemented, generating synchronous PMU exceptions is likely to be locally performance invasive. This means the invasiveness of enabling counters should be similar to the effect when synchronous PMU exceptions are not used. However, as the counter value approaches overflow, implementations might become more highly performance invasive. The value at which this occurs is IMPLEMENTATION DEFINED.

Note

The IMPLEMENTATION DEFINED invasiveness might include the PE disabling one or more performance optimizations such as multi-issue, out-of-order execution, and pipelining.

A software implication is that the performance invasiveness is proportional to the sampling interval. This can disproportionately affect profiling of rare events, because the population is smaller and therefore the interval will tend to be smaller.

## D13.2.2 A reasonable degree of inaccuracy

The Performance Monitors provide broadly accurate and statistically useful count information. To keep the implementation, validation, and performance overhead costs low, a reasonable degree of inaccuracy in the counts and the detection of overflow is acceptable. Arm does not define a reasonable degree of inaccuracy but recommends the following guidelines:

- Under normal operating conditions, all of the following apply:
- -The counters must present an accurate value of the count.
- -When FEAT\_SEBEP is implemented, the overflow of a counter in synchronous mode is observed by the instruction generating the event that causes the overflow, so long as other architectural conditions are met, such as the PMU exception is unmasked. For more information, see RNZLVW.
- In exceptional circumstances, such as enabling or disabling the counter, a change in Security state, or other boundary condition, it is acceptable for the count to be inaccurate.
- In exceptional microarchitectural circumstances, including when the event occurs rapidly in close succession, the overflow of a counter in synchronous mode might only be observed by a later instruction that also generates the event.

This means that there might be temporal inaccuracy in the generation of the PMU exception. This is also known as the shadow effect.

- Under very unusual, non-repeating pathological cases, the counts can be inaccurate. These cases are likely to occur as a result of asynchronous exceptions, such as interrupts, where the chance of a systematic error in the count is very unlikely.

Note

An implementation must not introduce inaccuracies that can be triggered systematically by the execution of normal pieces of software. For example, it is not reasonable for the count of branch behavior to be inaccurate when caused by a systematic error generated by the loop structure producing a dropping in branch count.

However, dropping a single branch count as the result of a rare interaction with an interrupt is acceptable.

The architecture does not permit these behaviors for events that specifically count architectural exceptional circumstances, such as a change in Exception level, for example, EXC\_TAKEN.

If FEAT\_SEBEP is implemented, then all of the following apply:

- Any shadow effect must be finite. An instruction generating the event must observe the overflow within a finite number of occurrences of the event after the counter has overflowed.
- In all circumstances, when a synchronous PMU exception is taken:
- -The counters present an accurate and precise value of the count, so that the exception is taken after the instruction that generated the overflow has retired.
- -The instruction that generated the exception by setting PSTATE.PPEND to 1 must have also generated the event.

Note

The instruction that generates the event that causes overflow might be executed when the PMU exception is disabled or masked, or the instruction causes the counter to increment by more than one. It is possible that on taking the PMU exception, the counter that overflowed has overshot. This means that after overflowing the counter counts past zero and the counter is nonzero when the PMU exception is taken. Any overshoot is reflected in the count value, and software can take the size of the overshoot value into account to determine the impact of exception masking and/or the shadow effect.

The permitted inaccuracy limits the possible uses of the Performance Monitors. In particular, the architecture does not define the point in a pipeline where the event counter is incremented, relative to the point where a read of the event counters is made. This means that pipelining effects can cause some imprecision, and can affect which events are counted.

This applies to both architectural and microarchitectural events, and can apply differently to different events. Arm recommends that is applied consistently between counters. For example, any boundary condition effects that apply to an event counter counting the CPU\_CYCLES event should apply in the same way to the cycle counter PMCCNTR\_EL0. However, this is not required.

Inaccuracies around exceptional events, such as enabling or disabling the counter, should be such that the inaccuracy is reduced by lengthening the sampling period.

Where a direct write to a Performance Monitors control register disables a counter, and is followed by a Context Synchronization event, any subsequent indirect read of the control register by the Performance Monitors to determine whether the counter is enabled will return the updated value. Any subsequent direct read of the counter or counter overflow status flags will return the value at the point the counter was disabled.

Note

The imprecision means that the counter might have counted an event around the time the counter was disabled, but does not allow the event to be observed as counted after the counter was disabled.

Achange of Security state can also affect the accuracy of the Performance Monitors, see Interaction with EL3.

In addition to this, entry to and exit from Debug state can disturb the normal running of the PE, causing further inaccuracy in the Performance Monitors. Disabling the counters while in Debug state limits the extent of this inaccuracy. An implementation can employ methods to limit this inaccuracy, for example by promptly disabling the counters during the Debug state entry sequence.

An implementation must document any particular scenarios where significant inaccuracies are expected.

If FEAT\_SEBEP is implemented, then implementations should document any specific microarchitectural circumstances when the shadow effect is likely to occur. For example for relatively frequent events such as INST\_RETIRED. Implementations should minimize any shadow effect for less common events, such as mispredicted branches and cache misses, eliminating the effect entirely in other than exceptional circumstances.

If all of the following apply, then PSTATE.PPEND will be set to 1 by an instruction B without any shadow effect:

- An instruction A is executed that is either a Context synchronization event or an MSR write to PSTATE.PM.
- When A completes execution, either:
- -The unsigned value of a PMU event counter &lt;n&gt; or the instruction counter (n == 32) is greater-than-or-equal to an IMPLEMENTATION SPECIFIC threshold value .
- -PMOVSSET\_EL0.P&lt;n&gt; is 1.
- B executes in program order after A .
- B meets all the conditions for an instruction in RNZLVW. See Synchronous exception-based event profiling.
- The PMU exception is enabled and unmasked from the instruction following A in program order up-to and including B .

The threshold value might depend on the event.

Note

The maximum threshold value is 0xFFFF\_FFFF\_FFFF\_FFFF so that a single event causes the counter to overflow and generate a PMU exception.

The threshold value is IMPLEMENTATION SPECIFIC to allow for implementations where the actual threshold might vary according to the type of event being monitored. In this case, it is not possible to document a single IMPLEMENTATION DEFINED threshold value. Arm recommends that implementations document the threshold values for specific events used in scenarios such as replay debugging, such as INST\_RETIRED, BR\_RETIRED, and PC\_WRITE\_RETIRED.