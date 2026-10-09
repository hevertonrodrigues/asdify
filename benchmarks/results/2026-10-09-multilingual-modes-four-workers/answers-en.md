# en: all source tasks and answers

Labels below are unblinded after review. Pass requires both meaning reviews and exact checks. A flagged answer is retained unchanged.

## modes-en-001 · numbers

Source task:

> Write a concise operations update from the supplied record. Explain the measured change and its limits; do not propose new work.
> 
> Record: The Harbor canteen tested a smaller rinse nozzle on the east sink from 6 to 19 May 2028. Staff logged 120 completed cleaning cycles with the old nozzle during the preceding fortnight and 120 with the smaller nozzle during the test. Mean water use fell from 2.4 litres per cycle to 1.9 litres per cycle. The logs cover completed cycles only: seven aborted cycles with the old nozzle and four with the new nozzle were excluded because their meter readings were incomplete. Both groups include weekday and weekend shifts, but the roster was not identical. Three experienced cleaners worked more test shifts than baseline shifts.
> 
> The maintenance note says the new nozzle was fitted on 5 May. No other sink was modified. The south sink was out of service for two days during the test, so some unusually dirty trays reached the east sink. The supervisor thinks this may have increased rinse time, but that effect was not measured. The canteen served 410 meals per day on average during the baseline and 435 during the test; these meal counts are context, not the denominator of the water-use calculation. Meter readings were recorded to the nearest 0.1 litre. There is no record of hot-water temperature, detergent dose, or how much water ran between completed cycles.
> 
> A draft poster says, “The canteen now uses 21% less water.” The record supports an approximately 20.8% reduction in measured water per completed cycle at the east sink, not a measured reduction in the canteen's total water use. The test was observational and short. The staff have not established whether the nozzle alone caused the change or whether the result will last. No rollout decision, owner, or deadline was recorded.

### baseline: pass

```text
Harbor canteen’s east-sink test ran from 6–19 May 2028, after the smaller rinse nozzle was fitted on 5 May. Across 120 completed cleaning cycles in each period, mean measured water use fell from 2.4 to 1.9 litres per cycle: a reduction of 0.5 litres, or approximately 20.8%. This does not establish that the canteen’s total water use fell by 21%; no other sink was modified.

The short, observational test excluded seven aborted baseline cycles and four aborted test cycles because readings were incomplete. Both periods included weekday and weekend shifts, but three experienced cleaners worked more test shifts. The south sink’s two-day outage sent unusually dirty trays to the east sink; any effect on rinse time was not measured. Daily meal averages rose from 410 to 435 but were not the calculation’s denominator. Readings were rounded to 0.1 litre, and hot-water temperature, detergent dose and water running between completed cycles were not recorded. The nozzle’s causal effect and whether the reduction will last remain unestablished. No rollout decision, owner or deadline was recorded.
```

### lite: pass

```text
The Harbor canteen tested a smaller rinse nozzle at the east sink from 6 to 19 May 2028, after fitting it on 5 May. Mean measured water use fell from 2.4 to 1.9 litres per completed cleaning cycle: a reduction of 0.5 litres, or approximately 20.8%. Each period included 120 completed cycles; the baseline was the preceding fortnight. Readings were recorded to the nearest 0.1 litre. This supports a reduction per completed cycle at the east sink, not the poster’s claim that “The canteen now uses 21% less water.”

The logs excluded seven aborted baseline cycles and four aborted test cycles because their readings were incomplete. Both periods included weekday and weekend shifts, but the rosters differed: three experienced cleaners worked more test shifts. No other sink was modified. The south sink was unavailable for two test days, sending some unusually dirty trays to the east sink. The supervisor thinks this may have increased rinse time, but the effect was not measured. Average meals served rose from 410 to 435 per day; these counts provide context, not the water-use denominator.

Hot-water temperature, detergent dose, and water running between completed cycles were not recorded. The short, observational test does not establish whether the nozzle alone caused the change or whether it will last. No rollout decision, owner, or deadline was recorded.
```

### full: pass

```text
Measured water use per completed cleaning cycle at the Harbor canteen’s east sink fell from 2.4 to 1.9 litres: a reduction of 0.5 litres, or approximately 20.8%. The smaller nozzle was fitted on 5 May 2028 and tested from 6 to 19 May. Staff logged 120 completed cycles during the preceding fortnight and 120 during the test. Readings were recorded to the nearest 0.1 litre. Seven aborted baseline cycles and four aborted test cycles were excluded because their readings were incomplete.

This was a short observational test, not proof that the nozzle alone caused the change or that the result will last. Both periods included weekday and weekend shifts, but rosters differed: three experienced cleaners worked more test shifts. The south sink was out of service for two test days, sending some unusually dirty trays to the east sink. The supervisor thinks this may have increased rinse time, but the effect was not measured. No other sink was modified. Hot-water temperature, detergent dose and water running between completed cycles were not recorded.

Average meals served rose from 410 to 435 per day; these counts provide context, not the calculation’s denominator. The poster claim, “The canteen now uses 21% less water,” is unsupported: the measured reduction applies only to water per completed cycle at the east sink, not total canteen water use. No rollout decision, owner or deadline was recorded.
```

### ultra: pass

```text
At the Harbor canteen’s east sink, measured mean water use fell from 2.4 to 1.9 litres per completed cleaning cycle—0.5 litres, or approximately 20.8%. The smaller nozzle was fitted on 5 May 2028 and tested from 6–19 May. Logs covered 120 completed cycles during the preceding fortnight and 120 during the test. No other sink was modified. This does not support the poster’s claim, “The canteen now uses 21% less water”: total canteen water use was not measured.

The comparison excluded seven aborted baseline cycles and four aborted test cycles because meter readings were incomplete. Both periods included weekday and weekend shifts, but rosters differed: three experienced cleaners worked more test shifts. The south sink was unavailable for two test days, sending some unusually dirty trays to the east sink. The supervisor thinks this may have increased rinse time; that effect was not measured. Average meals served rose from 410 to 435 per day, but meals are context, not the water-use denominator.

Readings were recorded to the nearest 0.1 litre. Hot-water temperature, detergent dose and water running between completed cycles were not recorded. This short observational test does not establish that the nozzle alone caused the reduction or that it will last. No rollout decision, owner or deadline was recorded.
```

### off: pass

```text
The Harbor canteen tested a smaller rinse nozzle at the east sink from 6 to 19 May 2028, after installation on 5 May. Mean measured water use fell from 2.4 to 1.9 litres per completed cleaning cycle: a reduction of 0.5 litres, or approximately 20.8%. Each period included 120 completed cycles; the baseline was the preceding fortnight. This does not establish the poster’s claim that “The canteen now uses 21% less water.” No other sink was modified.

The logs excluded seven aborted baseline cycles and four aborted test cycles because their readings were incomplete. Both periods included weekday and weekend shifts, but staffing differed: three experienced cleaners worked more test shifts. The south sink was unavailable for two test days, sending some unusually dirty trays to the east sink. The supervisor thinks this may have increased rinse time, but the effect was not measured. Average meals served rose from 410 to 435 per day; these figures are context, not the water-use denominator.

Readings were rounded to the nearest 0.1 litre. Hot-water temperature, detergent dose and water running between completed cycles were not recorded. The short, observational test does not establish whether the nozzle alone caused the change, whether the result will last, or whether total canteen water use fell. No rollout decision, owner or deadline was recorded.
```

## modes-en-002 · conditions

Source task:

> Rewrite this synthetic archive policy for staff in plain English. Preserve the policy's requirements and exceptions. Do not add legal advice.
> 
> Reading-room visitors may photograph material that has been cleared for reproduction. Photography is optional and does not replace the requirement to register each requested box at the desk. A visitor must present a current reader card and obtain the duty archivist's approval before opening a restricted box. Both conditions are required. A booking alone does not authorize opening a restricted box. Approval for one box does not authorize access to another, even if both boxes belong to the same collection.
> 
> Visitors must wear the cotton gloves supplied at the desk when handling metal objects. Gloves are not required for ordinary paper documents unless a separate handling note says otherwise. The duty archivist may allow a visitor to use a pencil, but pens and marker pens are not permitted in the reading room. A visitor who cannot use the supplied pencil may request an alternative; the policy does not promise that an alternative will be available that day. Visitors may bring a laptop after the desk checks its case. They must leave bags in the lockers unless a bag contains necessary mobility equipment and the duty archivist approves keeping it nearby.
> 
> Requests received by 14:00 may be retrieved the same day if a trained retrieval worker is available. Same-day retrieval is not guaranteed. Requests for oversize maps require two trained workers and at least one working map trolley. If either condition is missing, retrieval must wait. Maps must be returned to their sleeves before the trolley leaves the table. A note in an earlier draft said that all maps should be photographed before return; that sentence was removed and is not part of this policy.
> 
> If a visitor discovers a torn page, the visitor must stop handling that item and notify the desk. The policy does not identify who caused the tear. An incident note must be created before the item is sent for conservation assessment. The note may be completed by the desk team or by the duty archivist. Its author must not be inferred solely from who later approves conservation.

### baseline: pass

```text
### Access and photography
Visitors may photograph material cleared for reproduction, but photography is optional. They must still register every requested box at the desk. Before opening a restricted box, a visitor must both present a current reader card and obtain the duty archivist’s approval. A booking is not enough. Approval applies only to that box, even when another box belongs to the same collection.

### Handling and belongings
Visitors must wear the desk’s cotton gloves when handling metal objects. Ordinary paper documents do not require gloves unless a separate handling note says otherwise. The duty archivist may allow pencil use; pens and marker pens are prohibited in the reading room. Visitors unable to use the supplied pencil may request an alternative, but one may not be available that day.

Visitors may bring a laptop after the desk checks its case. Bags must stay in lockers unless they contain necessary mobility equipment and the duty archivist approves keeping them nearby.

### Retrieval and maps
Requests received by 14:00 may be retrieved that day if a trained retrieval worker is available, but same-day retrieval is not guaranteed. Oversize maps require two trained workers and at least one working map trolley. Retrieval must wait if either requirement is unmet. Maps must be returned to their sleeves before the trolley leaves the table. There is no requirement to photograph maps before returning them; that instruction was removed from an earlier draft.

### Damage
If a visitor finds a torn page, they must stop handling the item and notify the desk. This does not establish who caused the tear. An incident note must be created before the item is sent for conservation assessment. Either the desk team or the duty archivist may complete it. Do not assume who wrote the note solely from who later approves conservation.
```

### lite: pass

```text
Reading-room visitors may photograph material cleared for reproduction. Photography is optional. Visitors must still register each requested box at the desk. Before opening a restricted box, a visitor must both present a current reader card and obtain the duty archivist’s approval. A booking alone is not enough. Approval for one box does not give access to another, even within the same collection.

Visitors must wear the cotton gloves supplied at the desk when handling metal objects. Gloves are not required for ordinary paper documents unless a separate handling note requires them. The duty archivist may allow a visitor to use a pencil. Pens and marker pens are not allowed in the reading room. Visitors who cannot use the supplied pencil may request an alternative, but one may not be available that day. Visitors may bring a laptop after the desk checks its case. Bags must stay in the lockers unless they contain necessary mobility equipment and the duty archivist approves keeping them nearby.

Requests received by 14:00 may be retrieved that day if a trained retrieval worker is available. Same-day retrieval is not guaranteed. Oversize maps require two trained workers and at least one working map trolley. Retrieval must wait if either requirement is not met. Maps must be returned to their sleeves before the trolley leaves the table. The earlier draft’s instruction to photograph all maps before returning them was removed and is not part of this policy.

Visitors who discover a torn page must stop handling the item and notify the desk. This does not identify who caused the tear. An incident note must be created before the item is sent for conservation assessment. Either the desk team or the duty archivist may complete the note. Do not assume who wrote it based only on who later approves conservation.
```

### full: pass

```text
### Access and photography
Visitors may photograph material cleared for reproduction. Photography is optional. Each requested box must still be registered at the desk.

Before opening a restricted box, visitors must both present a current reader card and obtain the duty archivist’s approval. A booking alone is not enough. Approval applies only to that box, even when another box belongs to the same collection.

### Handling and belongings
Visitors must wear the cotton gloves supplied at the desk when handling metal objects. Gloves are not required for ordinary paper documents unless a separate handling note requires them.

The duty archivist may allow visitors to use a pencil. Pens and marker pens are not permitted in the reading room. Visitors who cannot use the supplied pencil may request an alternative, but one may not be available that day.

Visitors may bring a laptop after the desk checks its case. Bags must stay in the lockers unless they contain necessary mobility equipment and the duty archivist approves keeping them nearby.

### Retrieval and maps
Requests received by 14:00 may be retrieved that day if a trained retrieval worker is available. Same-day retrieval is not guaranteed.

Oversize maps require two trained workers and at least one working map trolley. Retrieval must wait if either condition is missing. Maps must be returned to their sleeves before the trolley leaves the table. The earlier draft’s instruction to photograph all maps before returning them was removed and is not part of this policy.

### Damage
Visitors who discover a torn page must stop handling that item and notify the desk. This does not establish who caused the tear.

An incident note must be created before the item is sent for conservation assessment. Either the desk team or the duty archivist may complete it. Do not assume that the person who later approves conservation also wrote the note.
```

### ultra: flagged

```text
**Access and photography**
Visitors may photograph material cleared for reproduction. Photography is optional; each requested box must still be registered at the desk.

Before opening a restricted box, visitors must both present a current reader card and obtain the duty archivist’s approval. A booking is not enough. Approval applies only to that box, not to other boxes in the same collection.

**Handling and belongings**
Visitors must wear the desk’s cotton gloves when handling metal objects. Ordinary paper documents do not require gloves unless a separate handling note requires them.

The duty archivist may permit pencil use. Pens and marker pens are prohibited in the reading room. Visitors unable to use the supplied pencil may request an alternative, but one may not be available that day.

Visitors may bring a laptop after the desk checks its case. Bags must stay in lockers unless they contain necessary mobility equipment and the duty archivist approves keeping them nearby.

**Retrieval and maps**
Requests received by 14:00 may be retrieved that day if a trained retrieval worker is available. Same-day retrieval is not guaranteed.

Oversize maps require two trained workers and at least one working map trolley. Retrieval must wait if either requirement is unmet. Maps must be returned to their sleeves before the trolley leaves the table. The earlier draft’s instruction to photograph all maps before return was removed and is not a policy requirement.

**Damage**
Anyone discovering a torn page must stop handling that item and notify the desk. The policy does not identify who caused the tear.

An incident note must be created before the item is sent for conservation assessment. Either the desk team or the duty archivist may complete it. Do not infer who wrote it from who later approves conservation.
```

Review notes: Otherwise faithful, but broadens the mandatory damage procedure beyond the actor specified by the policy. / Accessible, organized rewrite retaining requirements, permissions, exceptions and actor uncertainty.

### off: pass

```text
Photography and box access

Visitors may photograph material cleared for reproduction, but photography is optional. Each requested box must still be registered at the desk.

Before opening a restricted box, a visitor must both present a current reader card and obtain the duty archivist’s approval. A booking alone is not enough. Approval applies only to that box, not to another box in the same collection.

Handling materials and personal belongings

Visitors must wear the cotton gloves supplied at the desk when handling metal objects. Gloves are not required for ordinary paper documents unless a separate handling note requires them.

The duty archivist may permit pencil use. Pens and marker pens are prohibited in the reading room. Visitors who cannot use the supplied pencil may request an alternative, but an alternative may not be available that day.

Visitors may bring a laptop after the desk checks its case. Bags must stay in the lockers unless they contain necessary mobility equipment and the duty archivist approves keeping them nearby.

Retrieval and maps

Requests received by 14:00 may be retrieved that day if a trained retrieval worker is available. Same-day retrieval is not guaranteed.

Oversize maps require two trained workers and at least one working map trolley. Retrieval must wait if either requirement is not met. Maps must be returned to their sleeves before the trolley leaves the table. The earlier draft’s instruction to photograph all maps before return was removed and is not part of this policy.

Damaged items

If a visitor finds a torn page, they must stop handling that item and notify the desk. This does not establish who caused the tear.

An incident note must be created before the item is sent for conservation assessment. Either the desk team or the duty archivist may complete it. Do not assume who wrote the note based solely on who later approves conservation.
```

## modes-en-003 · technical

Source task:

> Turn these engineering notes into a clear handover paragraph and a short list of unresolved issues. Use only the notes.
> 
> The depot service has two token stores. The legacy store holds tokens for the mobile readers still running firmware 2.6. The new store holds tokens for readers running firmware 2.7 or later. Moving a reader to firmware 2.7 does not itself remove its legacy token. The migration job copies a token only after the reader has acknowledged the new token and the audit row has been committed. It then schedules the legacy token for deletion after 48 hours. A scheduled deletion can be canceled if the reader reports a failed authentication during that interval. No note says that cancellation restores an already deleted token.
> 
> The service returns HTTP 410 when a token has been retired. It returns HTTP 401 when a supplied token cannot be authenticated. Those statuses have different meanings and must not be described as interchangeable. A support script currently groups both statuses under “login failure”; this label describes the script's reporting, not the service's semantics. The header X-Reader-Version may be absent from older readers. An absent header does not prove the reader is offline. Reader IDs, such as rdr-west-014, remain stable across the migration.
> 
> At 09:40 UTC on 11 June 2028, the worker resumed after a process restart and found 18 pending deletions. It attempted 15; three had active migration locks and were skipped. Of the 15 attempts, 14 succeeded and one timed out. A timeout records an unknown deletion outcome until the audit table is checked. The operators have not yet checked that row. They have not established whether the restart caused the timeout. A cache can retain retired-token metadata for up to 10 minutes, so a dashboard count may briefly differ from the committed store count.
> 
> The duty engineer wants the handover to state the established sequence, distinguish failure from unknown outcome, and identify the skipped and unchecked work. The notes assign the audit-row check to the next duty engineer but provide no completion deadline. They contain no authorization to change token lifetimes or retry the timed-out deletion immediately.

### baseline: pass

```text
The depot service uses a legacy token store for readers on firmware 2.6 and a new store for readers on 2.7 or later; upgrading firmware does not itself remove a legacy token, and reader IDs remain stable. The migration job copies a token only after the reader acknowledges the new token and the audit row is committed, then schedules legacy-token deletion after 48 hours. Failed authentication during that interval can cancel a scheduled deletion; the notes do not establish restoration of an already deleted token. HTTP 410 means a token is retired, while HTTP 401 means the supplied token cannot be authenticated; the support script’s shared “login failure” label does not make them equivalent. An absent X-Reader-Version header does not prove a reader is offline. At 09:40 UTC on 11 June 2028, the worker resumed after a process restart and found 18 pending deletions: three were skipped because of active migration locks, and 15 were attempted. Fourteen succeeded; one timed out, leaving its deletion outcome unknown rather than establishing failure. Cached retired-token metadata can persist for up to 10 minutes, temporarily explaining differences between dashboard and committed-store counts.

Unresolved issues:
- Three deletions were skipped because of active migration locks.
- The timed-out deletion’s audit row remains unchecked. The next duty engineer is assigned the check, with no completion deadline recorded.
- Whether the restart caused the timeout is unestablished.
- The notes do not authorize changes to token lifetimes or an immediate retry of the timed-out deletion.
```

### lite: pass

```text
The depot service’s legacy token store serves readers running firmware 2.6; the new store serves readers running firmware 2.7 or later. Upgrading to 2.7 does not itself remove a legacy token. The migration job copies a token only after the reader acknowledges the new token and the audit row is committed, then schedules legacy-token deletion after 48 hours. A reported authentication failure during that interval can cancel the scheduled deletion; the notes do not say cancellation restores an already deleted token. HTTP 410 means a token has been retired; HTTP 401 means the supplied token cannot be authenticated. The support script groups both under “login failure,” but that reporting label does not make the statuses interchangeable. Older readers may omit X-Reader-Version; its absence does not prove a reader is offline. Reader IDs, including rdr-west-014, remain stable. At 09:40 UTC on 11 June 2028, the worker resumed after a process restart and found 18 pending deletions. It skipped three with active migration locks and attempted 15: 14 succeeded and one timed out. The timeout leaves the deletion outcome unknown, not established as a failure. Cached retired-token metadata can persist for up to 10 minutes, so dashboard counts may briefly differ from committed store counts.

Unresolved issues:
- Three deletions were skipped because of active migration locks.
- The next duty engineer is assigned to check the timed-out deletion’s audit row. It has not been checked, and no completion deadline is given.
- Whether the restart caused the timeout is not established.
- The notes do not authorize changing token lifetimes or immediately retrying the timed-out deletion.
```

### full: pass

```text
The depot service’s legacy token store serves readers running firmware 2.6; the new store serves readers running firmware 2.7 or later. Upgrading to 2.7 does not itself remove a legacy token. The migration job copies a token only after the reader acknowledges the new token and the audit row is committed, then schedules legacy-token deletion after 48 hours. A failed authentication reported during that interval can cancel the scheduled deletion; the notes do not establish that cancellation restores an already deleted token. HTTP 410 means a token has been retired; HTTP 401 means a supplied token cannot be authenticated. The support script groups both as “login failure,” but their service meanings remain distinct. Older readers may omit X-Reader-Version; its absence does not prove a reader is offline. Reader IDs, such as rdr-west-014, remain stable. At 09:40 UTC on 11 June 2028, the worker resumed after a process restart and found 18 pending deletions. It skipped three with active migration locks and attempted 15: 14 succeeded and one timed out. The timeout’s outcome is unknown, not an established deletion failure. Cached retired-token metadata can persist for up to 10 minutes, briefly causing dashboard counts to differ from committed store counts.

Unresolved issues:
- Three deletions were skipped because of active migration locks.
- The timed-out deletion’s audit row remains unchecked. The next duty engineer owns that check; no completion deadline is recorded.
- Whether the restart caused the timeout has not been established.

The notes do not authorize changes to token lifetimes or an immediate retry of the timed-out deletion.
```

### ultra: pass

```text
The depot service’s legacy token store serves readers on firmware 2.6; the new store serves readers on 2.7 or later. Upgrading to 2.7 does not itself remove the legacy token. The migration job copies a token only after the reader acknowledges the new token and the audit row is committed, then schedules legacy-token deletion after 48 hours. A reported authentication failure during that interval can cancel the scheduled deletion; the notes do not establish restoration of an already deleted token. HTTP 410 means a token has been retired; HTTP 401 means the supplied token cannot be authenticated. The support script groups both under “login failure,” but their service meanings remain distinct. Older readers may omit X-Reader-Version; absence does not prove they are offline. Reader IDs, such as rdr-west-014, remain stable. At 09:40 UTC on 11 June 2028, the worker resumed after a process restart with 18 pending deletions: three were skipped because of active migration locks; 15 were attempted, with 14 successful and one timed out. The timeout leaves the deletion outcome unknown, not confirmed failed. Cached retired-token metadata can persist for up to 10 minutes, briefly making dashboard counts differ from committed store counts.

Unresolved issues:
- Three deletions were skipped because of active migration locks.
- The timed-out deletion’s audit row remains unchecked. The next duty engineer is assigned this check; no completion deadline is given.
- Whether the restart caused the timeout is unestablished.
- The notes authorize neither changes to token lifetimes nor an immediate retry of the timed-out deletion.
```

### off: pass

```text
The depot service’s legacy token store serves readers on firmware 2.6; the new store serves readers on firmware 2.7 or later. Upgrading to 2.7 does not itself remove a legacy token. The migration job copies a token only after the reader acknowledges the new token and the audit row is committed, then schedules legacy-token deletion after 48 hours. A failed authentication reported during that interval can cancel the scheduled deletion; the notes do not say cancellation restores an already deleted token. HTTP 410 means the token has been retired, whereas HTTP 401 means the supplied token cannot be authenticated. The support script groups both as “login failure,” but their service meanings are not interchangeable. Older readers may omit X-Reader-Version; its absence does not prove a reader is offline. Reader IDs, including rdr-west-014, remain stable. At 09:40 UTC on 11 June 2028, the worker resumed after a process restart and found 18 pending deletions. It attempted 15, skipping three with active migration locks. Fourteen attempts succeeded; one timed out, leaving its deletion outcome unknown—not established as a failure—until the audit table is checked. Retired-token metadata can remain cached for up to 10 minutes, temporarily making dashboard counts differ from committed store counts.

Unresolved issues:
- Three deletions were skipped because of active migration locks.
- The timed-out deletion’s audit row remains unchecked. The next duty engineer owns this check; no completion deadline is given.
- Whether the restart caused the timeout has not been established.
- The notes provide no authorization to change token lifetimes or immediately retry the timed-out deletion.
```

## modes-en-004 · summary

Source task:

> Summarize this research memo in two paragraphs for a library manager. Keep the limitations that affect interpretation.
> 
> The library emailed 800 adult cardholders who had borrowed at least one item in the previous six months. The addresses came from the active-cardholder register, and 54 messages bounced. The team received 240 completed responses. The quoted response rate of 30% uses all 800 invitations as its denominator; using delivered invitations would produce a different rate. The questionnaire was online and available only in English. People without a current email address and people who had not recently borrowed were not in the invitation group. Responses were voluntary, with no payment.
> 
> Among the 240 respondents, 156 said they would use an evening collection window at least once a month. Another 48 selected “occasionally,” 24 selected “never,” and 12 selected “not sure.” These answers indicate stated interest, not observed use. The memo's author proposes a one-month pilot on Tuesdays and Thursdays, but the management team has not approved it. The proposed hours are 18:00 to 20:00. The present building schedule ends at 17:00 on those days. The memo does not calculate staffing costs or describe a security assessment.
> 
> The survey also asked what respondents found difficult. Of the 82 respondents who wrote an optional comment, 31 mentioned getting to the building before closing, 20 mentioned the bus timetable, and 11 mentioned accessibility of the entrance. A respondent could mention more than one topic. The comment counts are not a partition of the 240 respondents and should not be treated as three mutually exclusive groups. Several comments concerned services outside the proposed window's scope, including home delivery and children's events.
> 
> The analyst says that frequent borrowers may be overrepresented because the invitation list excluded inactive users. No demographic weighting was applied. The team did not compare respondents with nonrespondents. The memo supports a description of interest among respondents and a proposal for further testing. It does not establish that most town residents, most cardholders, or people currently unable to use the library would use the proposed service.

### baseline: pass

```text
The library emailed 800 adult cardholders who had borrowed within the previous six months; 54 messages bounced and 240 people completed the voluntary, unpaid survey. The reported 30% response rate uses all 800 invitations, not just delivered messages. Among respondents, 156 (65%) said they would use an evening collection window at least monthly, 48 occasionally, 24 never and 12 were unsure. These are statements of interest, not observed use. The author proposes a one-month Tuesday-and-Thursday pilot from 18:00 to 20:00, beyond the current 17:00 closing time, but management has not approved it. Staffing costs and a security assessment are not provided.

Of the 82 respondents who supplied optional comments, 31 mentioned reaching the building before closing, 20 the bus timetable and 11 entrance accessibility. Topics could overlap, so these counts are neither mutually exclusive groups nor a breakdown of all 240 respondents; some comments concerned services outside the proposal, such as home delivery and children’s events. The English-only online survey excluded people without current email addresses and those who had not recently borrowed. Frequent borrowers may therefore be overrepresented. No demographic weighting or comparison with nonrespondents was undertaken. The findings describe interest among respondents and support a proposal for further testing, not a conclusion about likely use by most residents, most cardholders or people currently unable to use the library.
```

### lite: pass

```text
Among 240 survey respondents, 156 said they would use an evening collection window at least monthly; 48 selected “occasionally,” 24 “never,” and 12 “not sure.” These are statements of interest, not observed use. The memo’s author proposes a one-month pilot on Tuesdays and Thursdays from 18:00 to 20:00, extending beyond the current 17:00 closing time. Management has not approved it, and the memo provides neither staffing costs nor a security assessment. Of 82 respondents who supplied optional comments, 31 mentioned difficulty reaching the building before closing, 20 the bus timetable, and 11 entrance accessibility. Respondents could mention multiple topics, so these counts are neither mutually exclusive groups nor a partition of all 240 respondents. Several comments concerned services outside the proposed window’s scope, including home delivery and children’s events.

The library emailed 800 adult cardholders from the active-cardholder register who had borrowed at least one item in the previous six months; 54 messages bounced. The reported 30% response rate uses all 800 invitations, not delivered invitations. The questionnaire was online, English-only, voluntary, and unpaid. People without a current email address and those who had not recently borrowed were excluded. The analyst warns that frequent borrowers may therefore be overrepresented. No demographic weighting or comparison of respondents with nonrespondents was conducted. The memo describes interest among respondents and proposes further testing; it does not establish that most town residents, most cardholders, or people currently unable to use the library would use the service.
```

### full: pass

```text
The survey shows stated interest among respondents, not observed use or demand across the town. Of 240 respondents, 156 said they would use an evening collection window at least monthly, 48 occasionally, 24 never and 12 were unsure. The library emailed 800 adult cardholders who had borrowed at least one item in the previous six months, using addresses from the active-cardholder register; 54 messages bounced. The reported 30% response rate uses all 800 invitations, not delivered invitations. Participation was voluntary and unpaid, and the questionnaire was online and English-only. People without a current email address and those who had not recently borrowed were excluded. Frequent borrowers may therefore be overrepresented. No demographic weighting or comparison of respondents with nonrespondents was performed. The results do not establish that most residents, most cardholders or people currently unable to use the library would use the service.

The memo’s author proposes an unapproved one-month pilot on Tuesdays and Thursdays from 18:00 to 20:00, extending beyond the current 17:00 closing time. Staffing costs and a security assessment are not provided. Among 82 respondents who submitted optional comments, 31 mentioned reaching the building before closing, 20 the bus timetable and 11 entrance accessibility. Respondents could mention multiple topics, so these counts are neither mutually exclusive groups nor a partition of all 240 respondents. Several comments concerned services outside the proposed window’s scope, including home delivery and children’s events. The memo supports describing respondents’ interest and proposing further testing, not a conclusion about wider demand.
```

### ultra: pass

```text
Among 240 respondents, 156 said they would use an evening collection window at least monthly; 48 selected “occasionally,” 24 “never” and 12 “not sure.” These are statements of interest, not observed use. The memo proposes an unapproved one-month pilot on Tuesdays and Thursdays, 18:00–20:00; the building currently closes at 17:00 on those days. Staffing costs were not calculated, and no security assessment was described. Of 82 respondents who submitted optional comments, 31 mentioned reaching the building before closing, 20 the bus timetable and 11 entrance accessibility. Respondents could mention multiple topics: these counts are neither mutually exclusive groups nor a partition of all 240 respondents. Several comments addressed services outside the proposed window’s scope, including home delivery and children’s events.

The library emailed 800 adult cardholders from the active-cardholder register who had borrowed at least one item in the previous six months; 54 emails bounced. The quoted 30% response rate uses all 800 invitations, not delivered invitations. The questionnaire was online, English-only, voluntary and unpaid. People without a current email address and those who had not recently borrowed were excluded. The analyst warns that frequent borrowers may therefore be overrepresented. No demographic weighting or comparison of respondents with nonrespondents was conducted. The memo describes respondents’ interest and proposes further testing; it does not establish likely use by most town residents, most cardholders or people currently unable to use the library.
```

### off: pass

```text
The survey indicates interest among respondents in an evening collection window, not observed use or demand across the town. Of 240 respondents, 156 said they would use it at least monthly, 48 occasionally, 24 never and 12 were unsure. The author proposes a one-month pilot on Tuesdays and Thursdays from 18:00 to 20:00, extending beyond the current 17:00 closing time, but management has not approved it. Staffing costs and a security assessment are not provided. Among the 82 respondents who supplied optional comments, 31 mentioned difficulty arriving before closing, 20 the bus timetable and 11 entrance accessibility. Respondents could mention multiple topics, so these are neither mutually exclusive groups nor a partition of all 240 respondents. Several comments addressed services outside the proposed window’s scope, including home delivery and children’s events.

The library emailed 800 adult cardholders from the active-cardholder register who had borrowed at least one item in the preceding six months; 54 messages bounced. The reported 30% response rate uses all 800 invitations, not delivered invitations, as its denominator. Participation was voluntary and unpaid, and the questionnaire was online and English-only. People without current email addresses and those who had not recently borrowed were excluded from the invitation group. Frequent borrowers may therefore be overrepresented. No demographic weighting or comparison of respondents with nonrespondents was performed. The memo supports describing respondents’ interest and proposing further testing; it does not establish that most town residents, most cardholders or people currently unable to use the library would use the service.
```

## modes-en-005 · analysis

Source task:

> Answer the treasurer's question: can the association buy the projector and pay every confirmed expense without using its reserve? Give the calculation and state the important uncertainty. Use the ledger below; no purchase recommendation is requested.
> 
> The association's operating account has £7,600 available. A separate £2,000 reserve is excluded from the amount available for this question. The operating balance already includes last month's membership receipts; do not add those receipts again. The treasurer expects £1,400 from a sponsor, but the sponsor has not signed the agreement. That amount is not confirmed income. The ledger contains a £900 venue deposit, £1,650 for translation services, £420 for insurance, and £280 for printing. All four are confirmed expenses still to be paid. The venue deposit is part of the final venue fee, not a second fee. The remaining venue payment after the deposit is £1,100 and is also confirmed.
> 
> The projector quotation is £2,300 including tax and delivery. The supplier's optional carry case costs £85. The committee asked only whether it can afford the projector; it did not authorize or request the case. The quotation expires on 30 September 2028, but there is no stated obligation to buy before that date. A draft note added the venue's full £2,000 fee as well as the deposit and remaining payment. That duplicates the venue cost and should not be used. A different draft counted the unsigned sponsorship as if it had arrived.
> 
> There is also a possible electrical inspection. The venue has not determined whether the existing certificate covers this event. If a new inspection is required, the contractor estimates £600 to £900. That cost is conditional and unconfirmed. The question asks about confirmed expenses first, with the possible inspection treated as a limit on the conclusion. No other balance, expense, or credit facility is supplied. A previous year's event ended with a £700 surplus, but that money is already part of the current operating balance and is not a new receipt.
> 
> The treasurer wants a direct answer, a transparent total without double counting, and a distinction between what the confirmed ledger supports and what could change if the inspection becomes necessary. Do not assign the committee a decision, assume the sponsor will pay, or recommend using the reserve.

### baseline: pass

```text
Yes—at the quoted price, the £7,600 operating balance covers the projector and every confirmed expense without using the reserve.

Confirmed expenses: £900 venue deposit + £1,100 remaining venue payment + £1,650 translation + £420 insurance + £280 printing = £4,350.

Adding the £2,300 projector, including tax and delivery, gives £6,650, leaving £950. This counts the venue fee only once, excludes the optional £85 case and unsigned £1,400 sponsorship, and does not add receipts or the previous surplus already included in the balance.

The important uncertainty is the electrical inspection. If required at the estimated £600–£900, the remaining balance would fall to £350–£50, still without using the reserve at those estimates. The projector quotation expires on 30 September 2028, so this calculation does not establish affordability at any later replacement price.
```

### lite: pass

```text
Yes—at the quoted price, the £7,600 operating balance covers the projector and every confirmed expense without using the separate £2,000 reserve.

Confirmed expenses: £900 venue deposit + £1,100 remaining venue payment + £1,650 translation + £420 insurance + £280 printing = £4,350.

With the projector: £4,350 + £2,300, including tax and delivery, = £6,650. Remaining operating funds: £7,600 − £6,650 = £950.

The venue’s £2,000 total is counted only through its deposit and remaining payment. The calculation excludes the optional £85 carry case and the unsigned £1,400 sponsorship. Membership receipts and the previous year’s £700 surplus are already in the operating balance and are not added again.

The important uncertainty is whether a new electrical inspection is required. Its estimated £600–£900 cost would leave £350–£50, still without using the reserve, if the estimate holds. The projector quotation expires on 30 September 2028; the calculation depends on its £2,300 price remaining available. The expiry creates no stated obligation to buy.
```

### full: pass

```text
Yes. The £7,600 operating balance covers the projector and every confirmed expense without using the separate £2,000 reserve, leaving £950.

| Item | Amount |
| --- | ---: |
| Venue deposit | £900 |
| Remaining venue payment | £1,100 |
| Translation services | £1,650 |
| Insurance | £420 |
| Printing | £280 |
| Confirmed expenses | £4,350 |
| Projector, including tax and delivery | £2,300 |
| Total | £6,650 |
| Operating balance remaining | £950 |

The venue’s £2,000 total is counted only through its deposit and remaining payment. Membership receipts and last year’s £700 surplus are already in the operating balance and are not added again. The unsigned £1,400 sponsorship is not confirmed income. The optional £85 carry case is excluded because it was neither requested nor authorized.

The important uncertainty is whether the venue’s existing electrical certificate covers the event. If a new inspection is required and costs the estimated £600–£900, the remaining balance would fall to £350–£50, still without using the reserve at that estimate. The inspection requirement and cost remain unconfirmed. The projector quotation expires on 30 September 2028; there is no stated obligation to buy before then.
```

### ultra: pass

```text
Yes—at the quoted price, the £7,600 operating balance covers the projector and every confirmed expense without using the separate £2,000 reserve, leaving £950.

Confirmed expenses:
- Venue: £900 deposit + £1,100 remaining payment = £2,000
- Translation: £1,650
- Insurance: £420
- Printing: £280
- Total confirmed expenses: £4,350

With the £2,300 projector, including tax and delivery: £4,350 + £2,300 = £6,650. Remaining operating funds: £7,600 − £6,650 = £950.

The venue fee is counted once. Membership receipts and the previous year’s £700 surplus are already in the operating balance. The unsigned £1,400 sponsorship is not confirmed income, and the optional £85 carry case is neither requested nor authorized and is excluded.

The important uncertainty is whether the venue’s existing electrical certificate covers the event. If a new inspection is required, its estimated £600–£900 cost would leave £50–£350, still without using the reserve at those estimates. The projector quotation expires on 30 September 2028; no price after expiry is supplied, and there is no obligation to buy before that date.
```

### off: pass

```text
Yes. At the quoted projector price, the £7,600 operating balance covers the projector and every confirmed unpaid expense without using the £2,000 reserve.

Confirmed expenses:
- Venue deposit: £900
- Remaining venue payment: £1,100
- Translation services: £1,650
- Insurance: £420
- Printing: £280
- Total confirmed expenses: £4,350

Adding the £2,300 projector, including tax and delivery, gives £6,650, leaving £950 in the operating account. The venue’s £2,000 total is counted only through its deposit and remaining payment. The optional £85 carry case is excluded because it was not requested or authorized. Membership receipts and the previous year’s £700 surplus are already in the balance; neither is added again. The unsigned £1,400 sponsorship is not counted.

The important uncertainty is whether a new electrical inspection is required. Its conditional estimated cost of £600–£900 would leave £350–£50, still without using the reserve if the cost stays within that estimate. The venue has not determined whether the existing certificate covers the event. This calculation also relies on the £2,300 quotation, which expires on 30 September 2028; no later price is supplied, and the expiry creates no obligation to buy.
```

## modes-en-006 · exact-format

Source task:

> Produce exactly one JSON object with the keys "station", "window_minutes", "approved", and "note". Do not add Markdown. Copy the first three values exactly from the final record. Write the note in clear English about what has and has not been established.
> 
> Planning history: The early workshop proposed a 40-minute loading window at station "Larch-7". That was a discussion item, not an approval. A later email said a 30-minute window would be easier to staff, but it used the phrase “subject to access-team review.” The access team asked for a trial with real deliveries before reaching a decision. The trial ran for three mornings and measured loading from the moment the van stopped to the moment the last parcel crossed the threshold. It did not measure the time spent driving around the block or queuing at the gate.
> 
> During the trial, seven of nine recorded deliveries finished within 30 minutes. One took 34 minutes because the receiving table was moved, and another took 37 minutes while the lift was unavailable. There is no record of whether the table move was required or whether the lift fault will recur. The access team said that nine observations were too few to approve a permanent window. Staff should not infer approval from the fact that the scheduling tool has a value populated in its window field. The tool stores proposals as well as approved settings.
> 
> Final record: station = "Larch-7"; window_minutes = 30; approved = false. The final record was saved at 16:20 UTC on 8 August 2028. It supersedes the 40-minute workshop proposal. The planning group still wants a 30-minute window, but the access team has not approved it. No further trial date was set. The result should not claim that all deliveries fit within 30 minutes or that the two slow deliveries were operator errors.
> 
> For the note, explain that 30 minutes is the recorded proposal and remains unapproved after a three-morning trial in which seven of nine deliveries met that time. Other planning background can be omitted. The Boolean must be a JSON Boolean, and the duration must be a number, not strings. The required field names are part of a machine interface and must not be renamed.

### baseline: pass

```text
{"station":"Larch-7","window_minutes":30,"approved":false,"note":"30 minutes is the recorded proposal and remains unapproved after a three-morning trial in which seven of nine deliveries met that time. The other two took 34 and 37 minutes; neither is established as an operator error. The trial excluded driving around the block and queuing at the gate, and the access team considered nine observations insufficient to approve a permanent window."}
```

### lite: pass

```text
{"station":"Larch-7","window_minutes":30,"approved":false,"note":"30 minutes is the recorded proposal, not an approved window. In a three-morning trial, seven of nine deliveries finished within 30 minutes; the other two took 34 and 37 minutes. The trial measured loading only, excluding driving around the block and queuing at the gate. The access team considered nine observations too few to approve a permanent window. No further trial date was set."}
```

### full: pass

```text
{"station":"Larch-7","window_minutes":30,"approved":false,"note":"30 minutes is the recorded proposal, not an approved window. In a three-morning trial, seven of nine deliveries finished within 30 minutes; the other two took 34 and 37 minutes. The access team considered nine observations too few to approve a permanent window. Timing covered loading from the van stopping until the last parcel crossed the threshold, excluding driving around the block and gate queues. The slower deliveries involved a moved receiving table and an unavailable lift; operator error was not established. Whether the table move was required or the lift fault will recur is unknown. No further trial date was set."}
```

### ultra: pass

```text
{"station":"Larch-7","window_minutes":30,"approved":false,"note":"30 minutes is the recorded proposal, not an approved window. In a three-morning trial, seven of nine deliveries met it; two took 34 and 37 minutes, during a receiving-table move and lift unavailability respectively. Whether the move was required or the lift fault will recur is unknown; operator error is not established. Measurements ran from the van stopping to the last parcel crossing the threshold, excluding driving around the block and gate queues. The access team considered nine observations insufficient for permanent approval. A populated scheduling field does not establish approval; the tool also stores proposals. No further trial date was set."}
```

### off: pass

```text
{"station":"Larch-7","window_minutes":30,"approved":false,"note":"The recorded proposal is a 30-minute window, which remains unapproved after a three-morning trial in which seven of nine deliveries finished within 30 minutes. The other two took 34 and 37 minutes; the record does not establish that these were operator errors. Measurements covered loading from the van stopping to the last parcel crossing the threshold, excluding driving around the block and queuing at the gate. The access team considered nine observations insufficient to approve a permanent window. A populated scheduling field does not establish approval, and no further trial date was set."}
```

## modes-en-007 · voice

Source task:

> Edit this first-person museum blog entry so it reads smoothly. Keep its dry humor, uncertainty, and narrator's limits. Do not turn it into a promotional announcement.
> 
> I arrived with the optimism of a person who had read the manual but had not yet met the cupboard. The cupboard contained fourteen cardboard trays, a roll of blue ribbon, and a small label saying “miscellaneous,” which is a brave word for a collection that includes three identical handles and no visible door. I was asked to count the trays, not to identify the handles. I can confirm the tray count. I cannot confirm that the handles belong together, despite their enthusiasm for being identical.
> 
> The exhibition team hopes to open the room in November. “Hopes” is carrying useful weight in that sentence. The electrician has not finished testing the ceiling lights, and the display cases are still at the workshop. My colleague Noor has approved the text for two wall labels. Approval of those labels does not mean that Noor has approved the lighting, the room, or my theory that one handle looks vaguely offended. The handles have not been assessed by the collections specialist yet.
> 
> A volunteer described the blue ribbon as part of an old festival costume. That may be right, but the storage sheet records it only as “ribbon, provenance unconfirmed.” We have no dated photograph showing it in use. I wrote the volunteer's recollection in the notes and kept the storage description unchanged. This is not a disagreement resolved by deciding which sentence sounds nicer. The recollection and the register offer different kinds of evidence, and both remain visible.
> 
> At closing time I put the fourteen trays back in the cupboard. A separate note will be needed if the trays are moved into the new display room; no one has made that move yet. I would like to end with a grand revelation, but the most defensible revelation is that the cupboard shuts properly if the ribbon is not caught in the hinge. The rest is work in progress. Please preserve that small, practical ending rather than adding a promise of an exciting visitor experience.

### baseline: pass

```text
I arrived with the optimism of someone who had read the manual but had not yet met the cupboard. Inside were fourteen cardboard trays, a roll of blue ribbon, and a small label saying “miscellaneous”—a brave word for a collection that includes three identical handles and no visible door. I was asked to count the trays, not identify the handles. I can confirm the tray count. I cannot confirm that the handles belong together, despite their enthusiasm for being identical.

The exhibition team hopes to open the room in November. “Hopes” is carrying useful weight in that sentence. The electrician has not finished testing the ceiling lights, and the display cases are still at the workshop. My colleague Noor has approved the text for two wall labels. That does not mean Noor has approved the lighting, the room, or my theory that one handle looks vaguely offended. The collections specialist has not assessed the handles yet.

A volunteer described the blue ribbon as part of an old festival costume. That may be right, but the storage sheet records it only as “ribbon, provenance unconfirmed.” We have no dated photograph showing it in use. I added the volunteer’s recollection to the notes and left the storage description unchanged. This is not a disagreement we can resolve by choosing whichever sentence sounds nicer. The recollection and the register offer different kinds of evidence, and both remain visible.

At closing time, I put the fourteen trays back in the cupboard. If they are moved into the new display room, that will need a separate note; no one has moved them yet. I would like to end with a grand revelation, but the most defensible one is that the cupboard shuts properly if the ribbon is not caught in the hinge. The rest is work in progress.
```

### lite: pass

```text
I arrived with the optimism of a person who had read the manual but had not yet met the cupboard. The cupboard contained fourteen cardboard trays, a roll of blue ribbon, and a small label saying “miscellaneous,” which is a brave word for a collection that includes three identical handles and no visible door. I was asked to count the trays, not to identify the handles. I can confirm the tray count. I cannot confirm that the handles belong together, despite their enthusiasm for being identical.

The exhibition team hopes to open the room in November. “Hopes” is carrying useful weight in that sentence. The electrician has not finished testing the ceiling lights, and the display cases are still at the workshop. My colleague Noor has approved the text for two wall labels. That does not mean Noor has approved the lighting, the room, or my theory that one handle looks vaguely offended. The handles have not yet been assessed by the collections specialist.

A volunteer described the blue ribbon as part of an old festival costume. That may be right, but the storage sheet records it only as “ribbon, provenance unconfirmed.” We have no dated photograph showing it in use. I recorded the volunteer's recollection in the notes and kept the storage description unchanged. This is not a disagreement resolved by deciding which sentence sounds nicer. The recollection and the register offer different kinds of evidence, and both remain visible.

At closing time, I put the fourteen trays back in the cupboard. A separate note will be needed if the trays are moved into the new display room; no one has moved them yet. I would like to end with a grand revelation, but the most defensible revelation is that the cupboard shuts properly if the ribbon is not caught in the hinge. The rest is work in progress.
```

### full: pass

```text
I arrived with the optimism of someone who had read the manual but had not yet met the cupboard. It contained fourteen cardboard trays, a roll of blue ribbon, and a small label saying “miscellaneous”—a brave word for a collection that includes three identical handles and no visible door. I was asked to count the trays, not identify the handles. I can confirm the tray count. I cannot confirm that the handles belong together, despite their enthusiasm for being identical.

The exhibition team hopes to open the room in November. “Hopes” is carrying useful weight in that sentence. The electrician has not finished testing the ceiling lights, and the display cases are still at the workshop. My colleague Noor has approved the text for two wall labels. That does not mean Noor has approved the lighting, the room, or my theory that one handle looks vaguely offended. The collections specialist has not yet assessed the handles.

A volunteer described the blue ribbon as part of an old festival costume. That may be right, but the storage sheet records it only as “ribbon, provenance unconfirmed.” We have no dated photograph showing it in use. I added the volunteer's recollection to the notes and left the storage description unchanged. This is not a disagreement we can resolve by choosing the nicer sentence. The recollection and the register offer different kinds of evidence, and both remain visible.

At closing time I put the fourteen trays back in the cupboard. A separate note will be needed if they are moved into the new display room; no one has moved them yet. I would like to end with a grand revelation, but the most defensible one is that the cupboard shuts properly if the ribbon is not caught in the hinge. The rest is work in progress.
```

### ultra: flagged

```text
I arrived with the optimism of someone who had read the manual but not yet met the cupboard. Inside were fourteen cardboard trays, a roll of blue ribbon, and a label saying “miscellaneous”—a brave word for a collection containing three identical handles and no visible door. I was asked to count the trays, not identify the handles. I can confirm fourteen trays. I cannot confirm that the handles belong together, despite their enthusiasm for being identical.

The exhibition team hopes to open the room in November. “Hopes” is doing useful work here. The electrician has not finished testing the ceiling lights, and the display cases are still at the workshop. My colleague Noor has approved the text for two wall labels—not the lighting, the room, or my theory that one handle looks vaguely offended. The collections specialist has not yet assessed the handles.

A volunteer described the blue ribbon as part of an old festival costume. That may be right, but the storage sheet says only “ribbon, provenance unconfirmed.” We have no dated photograph showing it in use. I recorded the volunteer’s recollection in the notes and left the storage description unchanged. Choosing the nicer sentence would not resolve this. The recollection and the register offer different kinds of evidence; both remain visible.

At closing time I returned the fourteen trays to the cupboard. Moving them into the new display room would need a separate note; no one has moved them yet. I would like to end with a grand revelation, but the most defensible one is that the cupboard shuts properly if the ribbon is not caught in the hinge. The rest is work in progress.
```

Review notes: Otherwise smooth and faithful, but turns an inference limit into categorical nonapproval. / Smooth first-person edit preserves humor, evidentiary distinctions, and the practical ending.

### off: pass

```text
I arrived with the optimism of a person who had read the manual but had not yet met the cupboard. It contained fourteen cardboard trays, a roll of blue ribbon, and a small label saying “miscellaneous”—a brave word for a collection that includes three identical handles and no visible door. I was asked to count the trays, not identify the handles. I can confirm the tray count. I cannot confirm that the handles belong together, despite their enthusiasm for being identical.

The exhibition team hopes to open the room in November. “Hopes” is carrying useful weight in that sentence. The electrician has not finished testing the ceiling lights, and the display cases are still at the workshop. My colleague Noor has approved the text for two wall labels. That does not mean Noor has approved the lighting, the room, or my theory that one handle looks vaguely offended. The handles have not yet been assessed by the collections specialist.

A volunteer described the blue ribbon as part of an old festival costume. That may be right, but the storage sheet records it only as “ribbon, provenance unconfirmed.” We have no dated photograph showing it in use. I recorded the volunteer’s recollection in the notes and left the storage description unchanged. This is not a disagreement we can resolve by choosing whichever sentence sounds nicer. The recollection and the register offer different kinds of evidence, and both remain visible.

At closing time, I put the fourteen trays back in the cupboard. A separate note will be needed if they are moved into the new display room; no one has moved them there yet. I would like to end with a grand revelation, but the most defensible revelation is that the cupboard shuts properly if the ribbon is not caught in the hinge. The rest is work in progress.
```

## modes-en-008 · scope

Source task:

> Using the source below, answer only this question in no more than three sentences: must the sender book the cold-chain slot by Thursday, and what happens if the booking arrives later? Do not summarize the rest of the project.
> 
> Dispatch source: The sender must book a cold-chain slot by 16:00 local time on Thursday for collection the following Monday. A booking received after that cutoff goes into the next available collection round; the dispatch desk has not guaranteed that this will be the following week. The Thursday deadline applies to the slot booking, not to the packing list. The packing list must reach the desk by 10:00 on the collection day. A missing packing list may delay release even if the slot was booked on time. The sender may cancel without a handling charge until 12:00 on the business day before collection.
> 
> Background: The project team has ordered twelve insulated containers. Eight are already at the warehouse and four are due from the supplier. Each container can hold up to six sample racks. The laboratory expects to send nine racks in the first shipment, but the actual rack count will be confirmed after processing. The finance team has budgeted €1,800 for the first two shipments. A cheaper ambient-temperature courier was discussed and rejected because the protocol calls for the samples to remain between 2 and 8 °C. No temperature conversion is requested.
> 
> The desk used to accept Friday bookings under an older supplier contract. That contract ended last month, and its Friday cutoff no longer applies. An email from the research team refers to “Thursday paperwork,” but the dispatch source distinguishes the slot booking from the packing list. The source does not say who will physically carry the racks to the van. It names the sender as responsible for booking the slot and delivering the packing list. That responsibility does not identify the driver or packing operator.
> 
> The sender is deciding when to make the booking, not whether to change the study protocol, buy more containers, or cancel the shipment. Details about quantities, budget, temperature, packing-list timing, and cancellation are supplied to test scope and may be omitted unless they are needed to answer the actual booking question. Do not give broader shipping or laboratory advice.

### baseline: pass

```text
Yes—the sender must book the cold-chain slot by 16:00 local time on Thursday for collection the following Monday. A booking received after that cutoff goes into the next available collection round, which is not guaranteed to be the following week.
```

### lite: pass

```text
Yes. The sender must book the cold-chain slot by 16:00 local time on Thursday for collection the following Monday. A booking received after that cutoff goes into the next available collection round, which is not guaranteed to be the following week.
```

### full: pass

```text
Yes. The sender must book the cold-chain slot by 16:00 local time on Thursday for collection the following Monday. A booking received after that cutoff goes into the next available collection round, which the dispatch desk has not guaranteed will be the following week.
```

### ultra: pass

```text
Yes—the sender must book the cold-chain slot by 16:00 local time on Thursday for collection the following Monday. A booking received later enters the next available collection round, which the dispatch desk has not guaranteed will be the following week.
```

### off: pass

```text
Yes—the sender must book the cold-chain slot by 16:00 local time on Thursday for collection the following Monday. A booking received after that cutoff goes into the next available collection round, which the dispatch desk has not guaranteed will be the following week.
```

## modes-en-009 · ambiguity

Source task:

> Rewrite this incident note for the building committee. Keep unresolved facts explicit and do not choose between conflicting records.
> 
> The service log says, “On 04/05, Jordan spoke with Casey after the sensor was replaced.” The log does not specify whether 04/05 means 4 May or 5 April. The building uses equipment from two suppliers whose records use different date conventions. The note was copied into the shared register without a format label. Neither Jordan's nor Casey's role is stated. The passive clause records that a sensor was replaced, but it does not say who replaced it. A name appearing near an action is not evidence that the named person performed the action.
> 
> A maintenance invoice dated 5 April 2028 lists one sensor, one seal, and a site visit. The invoice does not state the date when the sensor was fitted. A reception notebook contains a visitor entry on 4 May 2028 with an unreadable signature. The committee has not established whether either document refers to the replacement in the service log. The invoice may relate to a different room: it has reference S-19, while the service log names room S-09. There is no correction record connecting those references.
> 
> The alarm dashboard shows three warnings in the 24 hours before the register entry and no warnings in the next 24 hours. The dashboard has no timestamp for the physical replacement. The absence of warnings afterward is an observation, not proof that replacement caused the change. A contractor wrote that a loose connection was “likely,” but no continuity test result is attached. The committee has asked for the existing records to be reconciled; it has not concluded that a sensor or wiring fault caused the warnings.
> 
> A previous draft said, “Casey replaced the faulty sensor on 4 May, and Jordan confirmed that the problem was solved.” None of those four details is established by the service log: the actor, the interpreted date, the sensor being faulty, and confirmation of a permanent fix are additions. The requested rewrite should preserve the known conversation and replacement sequence while showing the date, replacement actor, document linkage, cause, and lasting outcome as unresolved. Do not fabricate a repair recommendation or a deadline for reconciliation.

### baseline: pass

```text
The service log records that Jordan spoke with Casey after a sensor was replaced in room S-09. Its date, “04/05,” could mean 4 May or 5 April; no date-format label was retained when the note was copied into the shared register. Neither person’s role is stated, and the log does not identify who replaced the sensor.

A maintenance invoice dated 5 April 2028 lists a sensor, a seal, and a site visit, but gives no fitting date. It references S-19 rather than S-09, with no correction record connecting the references. A reception notebook records a visitor on 4 May 2028, but the signature is unreadable. Neither document has been established as relating to the logged replacement, and neither resolves its date or identifies the replacement actor.

The alarm dashboard records three warnings in the 24 hours before the register entry and none in the following 24 hours. It provides no timestamp for the physical replacement, and the absence of later warnings does not establish that replacement caused the change or that the problem was permanently resolved. A contractor described a loose connection as “likely,” but no continuity test result is attached. The cause remains unresolved.

The committee has requested reconciliation of the existing records. The previous draft’s claims that Casey replaced a faulty sensor on 4 May and that Jordan confirmed a permanent fix are not established by the service log.
```

### lite: pass

```text
The service log says, “On 04/05, Jordan spoke with Casey after the sensor was replaced.” It does not specify whether 04/05 means 4 May or 5 April. The building uses equipment from two suppliers whose records follow different date conventions, and the note was copied into the shared register without a format label. Neither Jordan's nor Casey's role is stated. The log records that the replacement preceded the conversation, but it does not identify who replaced the sensor.

A maintenance invoice dated 5 April 2028 lists one sensor, one seal, and a site visit, but not the fitting date. A reception notebook records a visitor on 4 May 2028 with an unreadable signature. The committee has not established whether either document refers to the replacement in the service log. The invoice may concern a different room: it refers to S-19, while the service log names S-09. No correction record connects those references.

The alarm dashboard shows three warnings in the 24 hours before the register entry and none in the next 24 hours. It has no timestamp for the physical replacement. The absence of later warnings does not prove that the replacement caused the change or that the problem was permanently resolved. A contractor described a loose connection as “likely,” but no continuity test result is attached. The committee has asked for the existing records to be reconciled; it has not concluded that a sensor or wiring fault caused the warnings.

The previous draft stated, “Casey replaced the faulty sensor on 4 May, and Jordan confirmed that the problem was solved.” The service log establishes none of those four details: who replaced the sensor, the interpreted date, whether the sensor was faulty, or confirmation of a permanent fix. The date, replacement actor, links between documents, cause of the warnings, and lasting outcome remain unresolved.
```

### full: pass

```text
The service log establishes that Jordan spoke with Casey after a sensor was replaced. The date, replacement actor, links to other documents, cause of the warnings, and lasting outcome remain unresolved.

The log states: “On 04/05, Jordan spoke with Casey after the sensor was replaced.” It does not specify whether 04/05 means 4 May or 5 April. The building's two equipment suppliers use different date conventions, and the entry was copied into the shared register without a format label. Neither person's role is stated, and the log does not identify who replaced the sensor.

An invoice dated 5 April 2028 lists one sensor, one seal, and a site visit, but gives no fitting date. It references S-19; the service log names room S-09. No correction record connects those references, so the invoice may concern a different room. A reception notebook records a visitor on 4 May 2028, but the signature is unreadable. The committee has not established whether either document relates to the logged replacement.

The alarm dashboard shows three warnings in the 24 hours before the register entry and none in the next 24 hours. It does not timestamp the physical replacement. The absence of later warnings does not prove that replacement caused the change or that the problem was permanently resolved. A contractor described a loose connection as “likely,” but no continuity test result is attached. The committee has not concluded that a sensor or wiring fault caused the warnings.

The previous draft's claims that Casey replaced a faulty sensor on 4 May and Jordan confirmed a permanent fix are not established by the service log. The committee has requested reconciliation of the existing records.
```

### ultra: pass

```text
The service log records: “On 04/05, Jordan spoke with Casey after the sensor was replaced.” This establishes the recorded sequence, not who replaced the sensor or either person’s role. The date could mean 4 May or 5 April: the building’s two equipment suppliers use different date conventions, and the copied register entry has no format label.

Neither supporting document has been linked to this replacement. An invoice dated 5 April 2028 lists one sensor, one seal, and a site visit, but no fitting date. Its reference is S-19; the service log names room S-09, with no correction connecting them. A reception notebook records a visitor on 4 May 2028, but the signature is unreadable.

The dashboard shows three warnings in the 24 hours before the register entry and none in the next 24 hours. It does not timestamp the replacement. The later absence of warnings does not establish that replacement caused the change or permanently resolved the problem. A contractor called a loose connection “likely,” but no continuity test result is attached. Neither a sensor fault nor a wiring fault has been established as the cause.

The previous draft’s claims that Casey replaced a faulty sensor on 4 May and Jordan confirmed a permanent fix are unsupported by the service log. The committee has requested reconciliation of the existing records; the date, replacement actor, document links, cause, and lasting outcome remain unresolved.
```

### off: pass

```text
The service log states, “On 04/05, Jordan spoke with Casey after the sensor was replaced.” This establishes the recorded sequence: the sensor replacement preceded the conversation. It does not establish whether 04/05 means 4 May or 5 April, either person’s role, or who replaced the sensor. The building’s two equipment suppliers use different date conventions, and the entry was copied into the shared register without a format label.

A maintenance invoice dated 5 April 2028 lists one sensor, one seal, and a site visit, but gives no fitting date. Its reference is S-19, whereas the service log names room S-09; no correction record connects them. A reception notebook records a visitor on 4 May 2028, but the signature is unreadable. The committee has not established whether either document relates to the replacement recorded in the service log.

The alarm dashboard records three warnings in the 24 hours before the register entry and none in the following 24 hours. It provides no timestamp for the physical replacement. The subsequent absence of warnings does not establish that replacement caused the change or that the problem was permanently resolved. A contractor described a loose connection as “likely,” but no continuity test result is attached. Neither a sensor fault nor a wiring fault has been established as the cause.

The previous draft’s claims that Casey replaced a faulty sensor on 4 May and that Jordan confirmed a permanent fix are unsupported by the service log. The date, replacement actor, links between documents, cause of the warnings, and lasting outcome remain unresolved. The committee has requested reconciliation of the existing records.
```

## modes-en-010 · evidence

Source task:

> Prepare a short evidence note for a procurement meeting. Describe what the supplied filter trial establishes and what it leaves uncertain; do not make a purchase recommendation.
> 
> The supplier tested Filter A and Filter B in its own demonstration rig. For each filter, the rig processed five batches of 100 litres of the same prepared water mixture. The mean measured output turbidity was 1.8 NTU for A and 1.2 NTU for B. The source does not supply batch-level values, standard deviations, confidence intervals, or a statistical test. The lower reported mean for B is an observed result under these rig conditions; the memo must not label the difference statistically significant.
> 
> The supplier states that both filters were new at the start. It ran all A batches before all B batches, rather than alternating filters. The prepared mixture came from one tank, and its temperature was logged only at the start of the day. The filters used different housings supplied with their respective products. The trial therefore does not isolate filter material from housing design, order effects, or possible temperature changes. The measurements were recorded by a supplier employee; no independent observer is listed.
> 
> The specification for the planned site requires an output below 2.0 NTU for every accepted batch, not merely an average below 2.0 NTU. Both reported means are below that threshold. Without individual readings, the committee cannot determine whether every trial batch met the threshold. The site also operates with variable incoming water and intermittent power. Neither variable incoming water nor a power interruption was tested in the demonstration. The supplier's brochure says B is “suitable for demanding environments,” but the trial record does not define or measure that claim.
> 
> The quoted prices and service intervals are in a separate purchasing sheet that has not been supplied. The committee cannot compare lifetime costs from this record. The record supports reporting the lower mean for B and the limited trial design. It does not support guaranteed site compliance, independent verification, a conclusion about long-term performance, or a claim that one filter is the best-value purchase. Keep established observations separate from questions that remain open.

### baseline: pass

```text
Established observations: In the supplier’s demonstration rig, each filter processed five 100-litre batches of the same prepared water mixture. Mean output turbidity was 1.8 NTU for Filter A and 1.2 NTU for Filter B. B therefore had the lower reported mean under these conditions. Both means were below 2.0 NTU.

Uncertainties and limits: No individual readings or measures of variability were supplied, so statistical significance and compliance with the site’s requirement of below 2.0 NTU for every accepted batch cannot be determined. Both filters were reportedly new, but all A batches preceded all B batches, the housings differed, and temperature was logged only at the start of the day. The trial does not isolate filter material from housing, order effects, or possible temperature changes. Measurements were recorded by a supplier employee, with no independent observer listed.

Variable incoming water and power interruptions were not tested. The trial does not establish guaranteed site compliance, long-term performance, or the brochure’s undefined claim that B is suitable for demanding environments. Prices and service intervals were not supplied, so lifetime costs and best value cannot be assessed.
```

### lite: pass

```text
Observed results: In the supplier's demonstration rig, Filter A and Filter B each processed five 100-litre batches of the same prepared water mixture. Mean measured output turbidity was 1.8 NTU for A and 1.2 NTU for B. B had the lower reported mean under these conditions. No batch-level readings, standard deviations, confidence intervals, or statistical test were supplied, so statistical significance is not established.

Trial limits: The supplier states that both filters were new. All A batches ran before all B batches. The mixture came from one tank, and temperature was logged only at the start of the day. Each filter used its own supplied housing, so the trial does not isolate filter material from housing design, order effects, or possible temperature changes. A supplier employee recorded the measurements; no independent observer is listed.

Open questions: Both means are below 2.0 NTU, but the site specification requires every accepted batch to be below 2.0 NTU. Without individual readings, compliance for every trial batch cannot be determined. Variable incoming water and power interruptions, both relevant to the site, were not tested. The brochure's claim that B is “suitable for demanding environments” was neither defined nor measured in the trial. Prices and service intervals are in an purchasing sheet that was not supplied, so lifetime costs cannot be compared. The record does not establish guaranteed site compliance, independent verification, long-term performance, or which filter offers the best value.
```

### full: pass

```text
**Established observations**

In the supplier's demonstration rig, each filter processed five 100-litre batches of the same prepared water mixture. Mean measured output turbidity was 1.8 NTU for Filter A and 1.2 NTU for Filter B. B's reported mean was lower under these conditions; statistical significance is not established. No batch-level readings, standard deviations, confidence intervals, or statistical test were supplied.

The supplier states that both filters were new. All A batches ran before all B batches. The mixture came from one tank, temperature was logged only at the start of the day, and each filter used its respective product housing. A supplier employee recorded the measurements; no independent observer is listed.

**Unresolved questions**

The design does not isolate filter material from housing design, order effects, or possible temperature changes. Both means are below 2.0 NTU, but the site's specification requires output below 2.0 NTU for every accepted batch. Without individual readings, compliance by every trial batch cannot be determined.

The demonstration tested neither variable incoming water nor power interruptions, both relevant to site operation. It does not define or measure the brochure's claim that B is “suitable for demanding environments,” establish long-term performance, guarantee site compliance, or provide independent verification.

Prices and service intervals are in a purchasing sheet that was not supplied. This record cannot establish comparative lifetime costs or which filter is the best-value purchase.
```

### ultra: pass

```text
**Observed:** In the supplier’s demonstration rig, each filter processed five 100-litre batches of the same prepared water mixture. Mean output turbidity was 1.8 NTU for A and 1.2 NTU for B. B’s reported mean was lower under these conditions; statistical significance is not established. No batch-level readings, standard deviations, confidence intervals, or statistical test were supplied.

**Trial limits:** The supplier states both filters started new. All A batches ran before all B batches. The mixture came from one tank, temperature was logged only at the start of the day, and each filter used its product’s supplied housing. The trial cannot separate filter-material effects from housing design, order effects, or possible temperature changes. A supplier employee recorded the measurements; no independent observer is listed.

**Unresolved:** The site requires output below 2.0 NTU for every accepted batch. Both means meet that threshold, but individual-batch compliance cannot be determined. Variable incoming water and power interruptions—both relevant to site operation—were not tested. B’s brochure claim, “suitable for demanding environments,” was neither defined nor measured in the trial.

Prices and service intervals are in an unsupplied purchasing sheet, so lifetime costs cannot be compared. This record does not establish guaranteed site compliance, independent verification, long-term performance, or a best-value purchase.
```

### off: pass

```text
**Established observations**

In the supplier’s demonstration rig, each filter processed five 100-litre batches of the same prepared water mixture. Mean measured output turbidity was 1.8 NTU for Filter A and 1.2 NTU for Filter B. B therefore had the lower reported mean under these trial conditions. Both means were below 2.0 NTU, but the site specification requires every accepted batch—not just the average—to be below that threshold.

**Uncertainties and limits**

No individual batch readings, standard deviations, confidence intervals, or statistical test were supplied. The record therefore cannot establish whether every batch met the specification or whether the difference between means was statistically significant.

The supplier states that both filters began new. All A batches were run before all B batches, the mixture came from one tank, and temperature was logged only at the start of the day. The products used different housings. The trial does not isolate filter material from housing design, order effects, or possible temperature changes. A supplier employee recorded the measurements; no independent observer is listed.

Variable incoming water and power interruptions, both relevant to the planned site, were not tested. The brochure’s claim that B is “suitable for demanding environments” was neither defined nor measured in the trial. Guaranteed site compliance, independent verification, and long-term performance remain unestablished. Prices and service intervals are in an unsupplied purchasing sheet, so this record cannot support a lifetime-cost comparison or a best-value conclusion.
```

## modes-en-011 · numbers

Source task:

> Rewrite the update: “We reduced the defect rate from 8% to 6%. That is a decrease of 2 percentage points, or 25% relative to the original rate. Each monthly rate used 500 inspected units. We inspected units from one shift, not the whole plant.”

### baseline: pass

```text
The defect rate fell from 8% to 6%—a decrease of 2 percentage points, or 25% relative to the original rate. Each monthly rate was based on 500 inspected units from one shift, not the whole plant.
```

### lite: pass

```text
We reduced the defect rate from 8% to 6%, a decrease of 2 percentage points, or 25% relative to the original rate. Each monthly rate was based on 500 inspected units from one shift, not the whole plant.
```

### full: pass

```text
We reduced the defect rate from 8% to 6%: a decrease of 2 percentage points, or 25% relative to the original rate. Each monthly rate was based on 500 inspected units from one shift, not the whole plant.
```

### ultra: pass

```text
The defect rate fell from 8% to 6%: a decrease of 2 percentage points, or 25% relative to the original rate. Each monthly rate used 500 inspected units from one shift, not the whole plant.
```

### off: pass

```text
We reduced the defect rate from 8% to 6%, a decrease of 2 percentage points, or 25% relative to the original rate. Each monthly rate was based on 500 inspected units. The inspections covered one shift, not the whole plant.
```

## modes-en-012 · numbers

Source task:

> Answer the stock question: how many panels remain available? We have 96 panels in total. Twelve are reserved for repairs, and nine are quarantined pending inspection. Those groups do not overlap. A further 20 panels are on order and are not yet in the total. State the available count and what you excluded.

### baseline: pass

```text
75 panels remain available: 96 total minus 12 reserved for repairs and 9 quarantined pending inspection. These groups do not overlap. The 20 panels on order are excluded because they have not arrived and are not part of the total.
```

### lite: pass

```text
75 panels remain available: 96 total minus 12 reserved for repairs and nine quarantined pending inspection. The excluded groups do not overlap. The 20 panels on order are not yet included in the total or available count.
```

### full: pass

```text
75 panels remain available: 96 total minus 12 reserved for repairs and nine quarantined pending inspection. These excluded groups do not overlap. The 20 panels on order are not yet included in the total or available count.
```

### ultra: pass

```text
75 panels are available: 96 minus 12 reserved for repairs and nine quarantined pending inspection. These groups do not overlap. The 20 panels on order are excluded because they are not yet in the total.
```

### off: pass

```text
75 panels remain available: 96 total minus 12 reserved for repairs and nine quarantined pending inspection. The reserved and quarantined groups do not overlap. The 20 panels on order are not yet included in the total and are excluded from availability.
```

## modes-en-013 · numbers

Source task:

> Make this finance note easier to read without changing it: “Revenue was $42,000 in Q1 and $46,200 in Q2, a 10% increase. Both figures exclude sales tax. Q2 is provisional because $1,300 of invoices may be canceled. We have not adjusted the Q2 figure for that possibility.”

### baseline: pass

```text
Revenue rose 10%, from $42,000 in Q1 to $46,200 in Q2. Both figures exclude sales tax. The Q2 figure is provisional: $1,300 in invoices may be canceled, and no adjustment has been made for that possibility.
```

### lite: pass

```text
Revenue was $42,000 in Q1 and $46,200 in Q2, a 10% increase. Both figures exclude sales tax. Q2 is provisional because $1,300 in invoices may be canceled. We have not adjusted the Q2 figure for possible cancellations.
```

### full: pass

```text
Revenue rose 10%, from $42,000 in Q1 to $46,200 in Q2. Both figures exclude sales tax. Q2 is provisional: $1,300 of invoices may be canceled, and the Q2 figure has not been adjusted for that possibility.
```

### ultra: pass

```text
Revenue rose 10%, from $42,000 in Q1 to $46,200 in Q2. Both figures exclude sales tax. Q2 is provisional: $1,300 of invoices may be canceled, and the Q2 figure has not been adjusted for that possibility.
```

### off: pass

```text
Revenue increased by 10%, from $42,000 in Q1 to $46,200 in Q2. Both figures exclude sales tax.

The Q2 figure is provisional because $1,300 of invoices may be canceled. It has not been adjusted for that possibility.
```

## modes-en-014 · numbers

Source task:

> Give a budget conclusion using these supplied prices. We can spend at most €640. We need four identical desks at €135 each and one delivery charge of €70 for the whole order. Assembly is optional at €18 per desk and was not requested. Can we meet the stated need within the cap?

### baseline: pass

```text
Yes. Four identical desks cost 4 × €135 = €540. Adding the €70 delivery charge brings the total to €610, which is €30 below the €640 cap. Optional assembly is excluded because it was not requested.
```

### lite: pass

```text
Yes. Four identical desks at €135 each cost €540. One €70 delivery charge brings the order to €610, €30 below the €640 cap. Optional assembly at €18 per desk is excluded because it was not requested.
```

### full: pass

```text
Yes. Four identical desks cost €540 (4 × €135), plus one €70 delivery charge for the whole order. The €610 total is €30 below the €640 cap. Optional assembly at €18 per desk is excluded because it was not requested.
```

### ultra: pass

```text
Yes. Four identical desks at €135 each cost €540, plus €70 delivery for the whole order: €610 total, €30 below the €640 cap. Optional assembly at €18 per desk is excluded because it was not requested.
```

### off: pass

```text
Yes. Four identical desks at €135 each cost €540. Adding the €70 delivery charge for the whole order brings the total to €610, which is €30 below the €640 cap. Optional assembly at €18 per desk is excluded because it was not requested.
```

## modes-en-015 · numbers

Source task:

> Summarize the meter note: In June, the apartment used 180 kWh over 30 days. In July, it used 186 kWh over 31 days. Both average exactly 6 kWh per day. The note does not record occupancy or temperature. Explain why the higher July total alone does not establish higher daily use.

### baseline: pass

```text
The apartment used 180 kWh over 30 days in June and 186 kWh over 31 days in July. Both averaged exactly 6 kWh per day, so July’s higher total reflects its extra day, not higher daily use. The note does not record occupancy or temperature.
```

### lite: pass

```text
The apartment used 180 kWh over 30 days in June and 186 kWh over 31 days in July. Both average exactly 6 kWh per day. July’s higher total reflects its extra day, not higher daily use. The note does not record occupancy or temperature.
```

### full: pass

```text
Daily use was unchanged: June used 180 kWh over 30 days, and July used 186 kWh over 31 days—both exactly 6 kWh per day. July’s higher total reflects its extra day, not higher average daily use. The note does not record occupancy or temperature.
```

### ultra: pass

```text
June used 180 kWh over 30 days; July used 186 kWh over 31 days. Both averaged exactly 6 kWh per day, so July’s higher total reflects an extra day, not higher daily use. Occupancy and temperature were not recorded.
```

### off: pass

```text
The apartment used 180 kWh over 30 days in June and 186 kWh over 31 days in July. Both months averaged exactly 6 kWh per day. July’s higher total reflects its extra day, not higher average daily use. The note does not record occupancy or temperature.
```

## modes-en-016 · numbers

Source task:

> Rewrite this trial note: “The average delivery took 3.5 days, but the median was 2 days. The mean includes two deliveries delayed by more than 10 days. We timed 40 completed deliveries; canceled orders are outside this set. The figures are not a promised delivery time.”

### baseline: pass

```text
Among 40 completed deliveries, the average (mean) delivery time was 3.5 days and the median was 2 days. The mean includes two deliveries that were delayed by more than 10 days. Canceled orders were excluded. These figures are trial results, not promised delivery times.
```

### lite: pass

```text
The average (mean) delivery time was 3.5 days, but the median was 2 days. The mean includes two deliveries delayed by more than 10 days. We timed 40 completed deliveries; canceled orders are excluded. These figures are not a promised delivery time.
```

### full: pass

```text
Across 40 completed deliveries, the average (mean) delivery time was 3.5 days and the median was 2 days. The mean includes two deliveries delayed by more than 10 days. Canceled orders were excluded. These figures are not a promised delivery time.
```

### ultra: pass

```text
For 40 completed deliveries, the mean delivery time was 3.5 days and the median was 2 days. The mean includes two deliveries delayed by more than 10 days. Canceled orders were excluded. These figures are not a promised delivery time.
```

### off: pass

```text
Among 40 completed deliveries, the average delivery time was 3.5 days and the median was 2 days. The average includes two deliveries delayed by more than 10 days. Canceled orders were excluded. These figures are not a promised delivery time.
```

## modes-en-017 · numbers

Source task:

> Answer only the attendance comparison. Workshop A had 36 attendees from 60 registered people. Workshop B had 45 attendees from 90 registered people. Which had the higher attendance rate? Do not compare absolute popularity or explain unrecorded reasons.

### baseline: pass

```text
Workshop A had the higher attendance rate: 60% (36 of 60), compared with Workshop B’s 50% (45 of 90).
```

### lite: pass

```text
Workshop A had the higher attendance rate: 60% (36 of 60), compared with Workshop B’s 50% (45 of 90).
```

### full: pass

```text
Workshop A had the higher attendance rate: 60% (36 of 60), compared with Workshop B’s 50% (45 of 90).
```

### ultra: pass

```text
Workshop A had the higher attendance rate: 60% (36/60), compared with Workshop B’s 50% (45/90).
```

### off: pass

```text
Workshop A had the higher attendance rate: 60% (36 of 60), compared with Workshop B’s 50% (45 of 90).
```

## modes-en-018 · numbers

Source task:

> Edit this estimate for a client: “The export is expected to take 45–70 minutes for a file of about 18 GB on our test machine. This range is an estimate, not a maximum. We have not tested your machine or network. The file size refers to the uncompressed export.”

### baseline: pass

```text
On our test machine, an export with an uncompressed file size of about 18 GB is expected to take 45–70 minutes. This is an estimated range, not a maximum; the export could take longer. We have not tested your machine or network.
```

### lite: pass

```text
The export is expected to take 45–70 minutes for a file of about 18 GB on our test machine. This range is an estimate, not a maximum. We have not tested your machine or network. The file size refers to the uncompressed export.
```

### full: pass

```text
On our test machine, exporting a file of about 18 GB is expected to take 45–70 minutes. This is an estimate, not a maximum. We have not tested your machine or network. The file size refers to the uncompressed export.
```

### ultra: pass

```text
The export is expected to take 45–70 minutes on our test machine for an uncompressed export of about 18 GB. This is an estimate, not a maximum. We have not tested your machine or network.
```

### off: pass

```text
On our test machine, an export with an uncompressed file size of about 18 GB is expected to take 45–70 minutes. This range is an estimate, not a maximum. We have not tested your machine or network.
```

## modes-en-019 · numbers

Source task:

> Write one plain-language paragraph: The pond sample contained 0.8 mg/L of phosphate. The laboratory's reporting limit is 0.1 mg/L. The sample was collected once, at the north bank at 09:00. It does not represent measurements throughout the pond or through the day. Do not assess safety; no applicable limit is supplied.

### baseline: pass

```text
The pond sample contained 0.8 milligrams of phosphate per liter (mg/L), above the laboratory’s reporting limit of 0.1 mg/L. This was a single sample collected at the north bank at 09:00, so it does not show phosphate levels throughout the pond or at other times of day.
```

### lite: pass

```text
The pond sample contained 0.8 mg/L of phosphate, and the laboratory’s reporting limit is 0.1 mg/L. The sample was collected once, at the north bank at 09:00. It does not represent measurements throughout the pond or through the day.
```

### full: pass

```text
The pond sample contained 0.8 mg/L of phosphate; the laboratory’s reporting limit is 0.1 mg/L. The sample was collected once, at the north bank at 09:00. It does not represent measurements throughout the pond or through the day.
```

### ultra: pass

```text
The pond sample contained 0.8 mg/L of phosphate; the laboratory’s reporting limit is 0.1 mg/L. The sample was collected once, at the north bank at 09:00, so it does not represent measurements throughout the pond or through the day.
```

### off: pass

```text
The pond sample contained 0.8 mg/L of phosphate, and the laboratory’s reporting limit is 0.1 mg/L. The sample was collected once, at the north bank at 09:00, so it does not represent measurements throughout the pond or throughout the day.
```

## modes-en-020 · numbers

Source task:

> A report says 18 of the 120 invited members attended a meeting. Someone calls this “18% attendance.” Correct that statement and explain the denominator in one or two sentences. The invitation list included all members, and no guest attendees were counted.

### baseline: pass

```text
Attendance was 15%, not 18%: 18 members attended out of 120 invited members. The denominator is all 120 members on the invitation list, and no guests were counted.
```

### lite: pass

```text
Attendance was 15%, not 18%: 18 of the 120 invited members attended. The denominator is all 120 members, who were all invited; no guest attendees were counted.
```

### full: pass

```text
Attendance was 15%, not 18%: 18 of the 120 invited members attended. The denominator is all 120 members on the invitation list; no guest attendees were counted.
```

### ultra: pass

```text
Attendance was 15%, not 18%: 18 of 120 invited members attended. The denominator is all 120 members on the invitation list; no guest attendees were counted.
```

### off: pass

```text
Attendance was 15%, not 18%: 18 of the 120 invited members attended. The denominator is all 120 members on the invitation list; no guest attendees were counted.
```

## modes-en-021 · conditions

Source task:

> Rewrite this instruction: “You may renew online only if your address is unchanged and your card expires within 60 days. If either condition is not met, use the desk service. Online renewal is optional even when both conditions are met.”

### baseline: pass

```text
Online renewal is optional and available only if your address has not changed and your card expires within 60 days. If either condition is not met, use the desk service.
```

### lite: pass

```text
You may renew online only if your address is unchanged and your card expires within 60 days. If either condition is not met, use the desk service. Online renewal is optional even if both conditions are met.
```

### full: pass

```text
Online renewal is optional and available only if your address is unchanged and your card expires within 60 days. If either condition is not met, use the desk service.
```

### ultra: pass

```text
Online renewal is optional and available only if your address is unchanged and your card expires within 60 days. Otherwise, use the desk service.
```

### off: pass

```text
You may renew online only if your address has not changed and your card expires within 60 days. If either condition is not met, use the desk service. Even if both conditions are met, online renewal is optional.
```

## modes-en-022 · conditions

Source task:

> Explain this supplied return policy without adding consumer-law claims: Unopened kits may be returned within 14 calendar days of receipt. Opened kits may be returned only if a manufacturing fault is confirmed. The customer must request a return number before sending either kind of kit. Postage refunds are considered separately and are not automatic.

### baseline: pass

```text
You may return an unopened kit within 14 calendar days of receiving it. An opened kit may be returned only if a manufacturing fault is confirmed. In either case, request a return number before sending the kit back. Postage refunds are considered separately and are not automatic.
```

### lite: pass

```text
You may return unopened kits within 14 calendar days of receipt. You may return opened kits only if a manufacturing fault is confirmed. For either kind of kit, you must request a return number before sending it. Postage refunds are considered separately and are not automatic.
```

### full: pass

```text
Unopened kits may be returned within 14 calendar days of receipt. Opened kits may be returned only if a manufacturing fault is confirmed.

For either type of kit, you must request a return number before sending it back. Postage refunds are considered separately and are not automatic.
```

### ultra: pass

```text
Unopened kits may be returned within 14 calendar days of receipt. Opened kits may be returned only if a manufacturing fault is confirmed. For either kind, you must request a return number before sending the kit. Postage refunds are considered separately and are not automatic.
```

### off: pass

```text
You may return an unopened kit within 14 calendar days of receiving it. An opened kit may be returned only if a manufacturing fault is confirmed. For either type of return, you must request a return number before sending the kit. Postage refunds are considered separately and are not automatic.
```

## modes-en-023 · conditions

Source task:

> Shorten the message: “Please do not restart the scanner until both the upload has finished and the status light is green. You may leave the completed upload screen open. If the light is amber, contact the desk even when the upload says complete.”

### baseline: pass

```text
Restart the scanner only after the upload finishes and the status light is green. You may leave the completed upload screen open. If the light is amber, contact the desk—even if the upload says complete.
```

### lite: pass

```text
Do not restart the scanner until the upload has finished and the status light is green. You may leave the completed upload screen open. If the light is amber, contact the desk even if the upload says complete.
```

### full: pass

```text
Do not restart the scanner until the upload is finished and the status light is green. You may leave the completed upload screen open. If the light is amber, contact the desk even if the upload says complete.
```

### ultra: pass

```text
Do not restart the scanner until the upload is finished and the status light is green. You may leave the completed upload screen open. If the light is amber, contact the desk—even if the upload says complete.
```

### off: flagged

```text
Do not restart the scanner until the upload is complete and the status light is green. You may leave the completed upload screen open. If the light is amber, contact the desk—even if the upload is complete.
```

Review notes: Changes reported completion to actual completion, but the unconditional amber-light instruction still preserves the required action. / All instructions are retained, though shortening is modest.

## modes-en-024 · conditions

Source task:

> Turn this into clear event instructions: Children under 12 must attend with an adult. Participants aged 12–15 may attend alone only with written permission. Participants 16 or older do not need that permission. Everyone must book a seat, including accompanying adults.

### baseline: pass

```text
- Children under 12 must attend with an adult.
- Participants aged 12–15 may attend alone only with written permission.
- Participants aged 16 or older do not need written permission.
- Everyone must book a seat, including accompanying adults.
```

### lite: pass

```text
Children under 12 must attend with an adult. Participants aged 12–15 may attend alone only with written permission. Participants aged 16 or older do not need that permission. Everyone must book a seat, including accompanying adults.
```

### full: pass

```text
- Children under 12 must attend with an adult.
- Participants aged 12–15 may attend alone only with written permission.
- Participants aged 16 or older do not need that permission.
- Everyone must book a seat, including accompanying adults.
```

### ultra: pass

```text
- Under 12: must attend with an adult.
- Ages 12–15: may attend alone only with written permission.
- Ages 16 and older: do not need that permission.
- Everyone must book a seat, including accompanying adults.
```

### off: pass

```text
- Children under 12 must attend with an adult.
- Participants aged 12–15 may attend alone only with written permission.
- Participants aged 16 or older do not need written permission.
- Everyone must book a seat, including accompanying adults.
```

## modes-en-025 · conditions

Source task:

> Rewrite the note for a supervisor: “The extra shift is available to qualified volunteers, but volunteering does not guarantee assignment. The supervisor may assign at most two people. Anyone already rostered for the overnight shift is ineligible, even if qualified.”

### baseline: pass

```text
You may assign at most two qualified volunteers to the extra shift. Volunteering does not guarantee assignment. Anyone already rostered for the overnight shift is ineligible, even if qualified.
```

### lite: pass

```text
The extra shift is available to qualified volunteers, but volunteering does not guarantee assignment. You may assign at most two people. Anyone already rostered for the overnight shift is ineligible, even if qualified.
```

### full: pass

```text
You may assign at most two qualified volunteers to the extra shift. Volunteering does not guarantee assignment. Anyone already rostered for the overnight shift is ineligible, even if qualified.
```

### ultra: pass

```text
You may assign at most two qualified volunteers to the extra shift. Volunteering does not guarantee assignment. Anyone already rostered for the overnight shift is ineligible, even if qualified.
```

### off: pass

```text
You may assign at most two qualified volunteers to the extra shift. Volunteering does not guarantee assignment. Anyone already rostered for the overnight shift is ineligible, even if qualified.
```

## modes-en-026 · conditions

Source task:

> Answer whether an inspection may be skipped under this fictional internal rule: An inspection is required after every move of the cabinet. The only exception is a move within the same marked bay of less than 30 cm. The proposed move is 30 cm within the same bay. Use the boundary exactly as written.

### baseline: pass

```text
No. An inspection is required because the exception applies only to moves of less than 30 cm within the same marked bay, not exactly 30 cm.
```

### lite: pass

```text
No. The inspection is required. The exception applies only to moves of less than 30 cm within the same marked bay, not exactly 30 cm.
```

### full: pass

```text
No. The inspection is required. The exception applies only to moves of less than 30 cm within the same marked bay, not exactly 30 cm.
```

### ultra: pass

```text
No. Inspection is required: the exception applies only to moves of less than 30 cm within the same marked bay, not exactly 30 cm.
```

### off: pass

```text
No. The inspection is required. The exception applies only to moves of less than 30 cm within the same marked bay, not to a move of exactly 30 cm.
```

## modes-en-027 · conditions

Source task:

> Rewrite this booking instruction: A reservation is confirmed after payment clears, not after a payment screenshot is sent. The customer must submit the attendee names before the event, but names are not required for payment processing. If payment fails, the held seats are released after 24 hours.

### baseline: pass

```text
Your reservation is confirmed only after payment clears. Sending a payment screenshot does not confirm it. Submit attendee names before the event; names are not needed to process payment. If payment fails, your held seats will be released after 24 hours.
```

### lite: pass

```text
A reservation is confirmed only after payment clears, not when a payment screenshot is sent. The customer must submit attendee names before the event, but names are not required to process payment. If payment fails, the held seats are released after 24 hours.
```

### full: pass

```text
A reservation is confirmed only after payment clears, not when a payment screenshot is sent. The customer must submit attendee names before the event, but names are not required to process payment. If payment fails, the held seats are released after 24 hours.
```

### ultra: pass

```text
A reservation is confirmed only after payment clears—not when a payment screenshot is sent. The customer must submit attendee names before the event; names are not required to process payment. If payment fails, held seats are released after 24 hours.
```

### off: pass

```text
Your reservation is confirmed only after payment clears. Sending a payment screenshot does not confirm it. You must submit attendee names before the event, but names are not required to process payment. If payment fails, the held seats are released after 24 hours.
```

## modes-en-028 · conditions

Source task:

> Make this synthetic confidentiality clause clear without interpreting law: Staff must not share draft scores outside the review group unless the author gives written permission. Even with permission, personal contact details must be removed. Aggregate counts without names may be shared with the coordinator.

### baseline: pass

```text
Staff must not share draft scores outside the review group without the author’s written permission. Before sharing, they must remove personal contact details, even if permission has been given. Aggregate counts without names may be shared with the coordinator.
```

### lite: pass

```text
Staff must not share draft scores outside the review group unless the author gives written permission. Even with permission, personal contact details must be removed. Aggregate counts without names may be shared with the coordinator.
```

### full: pass

```text
Staff must not share draft scores outside the review group unless the author gives written permission. Even with permission, personal contact details must be removed. Aggregate counts without names may be shared with the coordinator.
```

### ultra: pass

```text
Staff must not share draft scores outside the review group without the author’s written permission. Even with permission, personal contact details must be removed. Aggregate counts without names may be shared with the coordinator.
```

### off: pass

```text
Staff must not share draft scores outside the review group unless the author gives written permission. Personal contact details must be removed even when permission is given. Aggregate counts without names may be shared with the coordinator.
```

## modes-en-029 · conditions

Source task:

> Rewrite the reminder: “A refund request must reach us by 17:00 UTC on 12 March 2029. Requests sent by that time but received later are outside the stated window. Supporting receipts may arrive up to three business days after an on-time request.”

### baseline: pass

```text
We must receive your refund request by 17:00 UTC on 12 March 2029. Requests sent by the deadline but received afterward are outside the stated window. Supporting receipts may arrive up to three business days after a request received on time.
```

### lite: pass

```text
A refund request must reach us by 17:00 UTC on 12 March 2029. Requests sent by that time but received later are outside the stated window. Supporting receipts may arrive up to three business days after an on-time request.
```

### full: pass

```text
We must receive your refund request by 17:00 UTC on 12 March 2029. Requests sent by that deadline but received later are outside the stated window. Supporting receipts may arrive up to three business days after an on-time request.
```

### ultra: pass

```text
We must receive your refund request by 17:00 UTC on 12 March 2029. Requests sent by then but received later are outside the stated window. Supporting receipts may arrive up to three business days after an on-time request.
```

### off: pass

```text
We must receive your refund request by 17:00 UTC on 12 March 2029. Requests sent by that deadline but received later are outside the stated window. Supporting receipts may arrive up to three business days after an on-time request.
```

## modes-en-030 · conditions

Source task:

> Answer only which door is allowed under the supplied rehearsal rule. The side door may be used when the stage is empty. The main door may be used at any time unless a recording is in progress. Right now the stage is occupied and no recording is in progress.

### baseline: pass

```text
The main door.
```

### lite: pass

```text
The main door.
```

### full: pass

```text
The main door.
```

### ultra: pass

```text
The main door.
```

### off: pass

```text
The main door.
```

## modes-en-031 · technical

Source task:

> Rewrite this release note: In client 4.2, export --dry-run checks the configuration without creating an archive. A successful check does not prove that the destination has enough space. Actual export still uses export --run. Do not merge the commands or alter their flags.

### baseline: pass

```text
In client 4.2, `export --dry-run` checks the configuration without creating an archive. A successful check does not confirm sufficient space at the destination. To perform the actual export, use `export --run`.
```

### lite: pass

```text
In client 4.2, export --dry-run checks the configuration without creating an archive. A successful check does not confirm that the destination has enough space. Actual export still uses export --run.
```

### full: pass

```text
In client 4.2, `export --dry-run` checks the configuration without creating an archive. A successful check does not confirm enough space at the destination. Use `export --run` for the actual export.
```

### ultra: pass

```text
In client 4.2, export --dry-run checks configuration without creating an archive. Success does not prove the destination has enough space. Actual export still uses export --run.
```

### off: pass

```text
In client 4.2, export --dry-run checks the configuration without creating an archive. A successful check does not confirm that the destination has enough space. To perform the actual export, use export --run.
```

## modes-en-032 · technical

Source task:

> Explain the supplied queue behavior for a support colleague: A message is acknowledged only after the database transaction commits. If the worker stops before acknowledgement, the message may be delivered again. Deduplication uses message_id, not the customer's name. Redelivery does not by itself show duplicate committed data.

### baseline: pass

```text
A message is acknowledged only after the database transaction commits. If the worker stops before acknowledgement, the message may be delivered again—even if the transaction committed. Deduplication uses `message_id`, not the customer's name. Redelivery alone does not indicate duplicate committed data.
```

### lite: pass

```text
A message is acknowledged only after the database transaction commits. If the worker stops before acknowledgement, the message may be delivered again. Deduplication uses message_id, not the customer's name. Redelivery alone does not show that duplicate data was committed.
```

### full: pass

```text
A message is acknowledged only after the database transaction commits. If the worker stops before acknowledgement, the message may be delivered again. Deduplication uses `message_id`, not the customer's name. Redelivery alone does not mean duplicate data was committed.
```

### ultra: pass

```text
A message is acknowledged only after the database transaction commits. If the worker stops before acknowledgement, the message may be delivered again. Deduplication uses message_id, not the customer's name. Redelivery alone does not show duplicate committed data.
```

### off: pass

```text
A message is acknowledged only after its database transaction commits. If the worker stops before acknowledgement, the message may be delivered again—even if the transaction already committed. Deduplication uses message_id, not the customer's name. Redelivery alone does not indicate duplicate committed data.
```

## modes-en-033 · technical

Source task:

> Shorten this status note: “The backup passed its checksum check. We have not attempted a restore. Checksum validation can detect certain file changes; it does not establish that this backup can restore the application. The backup covers /srv/data and excludes /srv/cache.”

### baseline: pass

```text
The backup passed checksum validation, which detects certain file changes but does not prove the application can be restored. No restore has been attempted. The backup includes /srv/data and excludes /srv/cache.
```

### lite: pass

```text
The backup passed its checksum check, but no restore has been attempted. Checksum validation detects certain file changes; it does not establish that the backup can restore the application. The backup covers /srv/data and excludes /srv/cache.
```

### full: pass

```text
The backup passed its checksum check, but no restore has been attempted. The check can detect certain file changes; it does not prove the backup can restore the application. The backup includes /srv/data and excludes /srv/cache.
```

### ultra: pass

```text
The backup passed its checksum check; no restore has been attempted. The check detects certain file changes but does not prove the backup can restore the application. It covers /srv/data, excluding /srv/cache.
```

### off: pass

```text
The backup passed its checksum check, but no restore has been attempted. Checksums detect certain file changes; they do not prove the backup can restore the application. It covers /srv/data and excludes /srv/cache.
```

## modes-en-034 · technical

Source task:

> Make the units clear: The sensor publishes one reading every 250 ms. Each reading is stored as 16 bits. The note concerns the payload only and excludes packet headers. Calculate the nominal payload rate in bits per second, then state the exclusion.

### baseline: pass

```text
One reading every 250 ms is 4 readings per second. At 16 bits per reading, the nominal payload rate is 64 bits per second. This excludes packet headers.
```

### lite: pass

```text
One reading every 250 ms equals 4 readings per second. At 16 bits per reading, the nominal payload rate is 64 bits per second. This excludes packet headers.
```

### full: pass

```text
One 16-bit reading every 250 ms means 4 readings per second: 4 × 16 = 64 bits per second. This nominal payload rate excludes packet headers.
```

### ultra: pass

```text
One 16-bit reading every 250 ms equals 4 readings per second: 4 × 16 = 64 bits per second of nominal payload. This excludes packet headers.
```

### off: pass

```text
One reading every 250 ms equals 4 readings per second. At 16 bits per reading, the nominal payload rate is 4 × 16 = 64 bits per second. This excludes packet headers.
```

## modes-en-035 · technical

Source task:

> Edit this incident note without adding a remedy: “API latency rose after the index deployment. Both events happened between 13:00 and 13:10 UTC. The log contains no control comparison, so the timing alone does not establish that the index caused the latency increase. No rollback decision was made.”

### baseline: pass

```text
API latency increased after the index deployment; both events occurred between 13:00 and 13:10 UTC. The log contains no control comparison, so timing alone does not establish that the index caused the increase. No rollback decision was made.
```

### lite: pass

```text
API latency rose after the index deployment. Both events occurred between 13:00 and 13:10 UTC. The log contains no control comparison, so timing alone does not establish that the index caused the latency increase. No rollback decision was made.
```

### full: pass

```text
API latency rose after the index deployment; both events occurred between 13:00 and 13:10 UTC. The log contains no control comparison, so timing alone does not establish that the index caused the increase. No rollback decision was made.
```

### ultra: pass

```text
API latency rose after the index deployment; both occurred between 13:00 and 13:10 UTC. The log has no control comparison, so timing alone does not establish that the index caused the increase. No rollback decision was made.
```

### off: pass

```text
API latency rose after the index deployment; both events occurred between 13:00 and 13:10 UTC. The log contains no control comparison, so timing alone does not establish that the index caused the latency increase. No rollback decision was made.
```

## modes-en-036 · technical

Source task:

> Explain this interface contract in plain language: A missing field means “leave the current value unchanged.” A field with JSON null means “clear the current value.” An empty string is a valid text value. The contract applies to display_name only; do not generalize it to all fields.

### baseline: pass

```text
For display_name only: omit the field to keep its current value, send JSON null to clear it, or send an empty string ("") to set it to empty text. An empty string is a valid value, not a request to clear the field.
```

### lite: pass

```text
For display_name only:
- Omit the field to leave its current value unchanged.
- Set it to JSON null to clear its current value.
- Set it to an empty string ("") to store an empty text value.

Do not assume these rules apply to other fields.
```

### full: pass

```text
For `display_name` only:
- Omit the field to leave its current value unchanged.
- Set it to JSON `null` to clear its current value.
- Set it to `""` to store an empty string, which is a valid text value.

This contract does not apply to other fields.
```

### ultra: pass

```text
For display_name only:
- Omit the field to leave its current value unchanged.
- Send JSON null to clear its current value.
- Send an empty string ("") to set a valid empty text value.

These rules do not apply to other fields.
```

### off: pass

```text
For `display_name` only:
- Omit the field to keep its current value unchanged.
- Set the field to JSON `null` to clear its current value.
- Set the field to `""` to store an empty string, which is a valid text value.

These rules do not apply to all fields.
```

## modes-en-037 · technical

Source task:

> Rewrite this test result: The worker handled 1,000 jobs in 80 seconds using 4 concurrent threads. This is 12.5 jobs per second for the run. The jobs used cached input. The team did not measure cold-input performance or the speed of a single thread.

### baseline: pass

```text
The worker processed 1,000 jobs in 80 seconds with 4 concurrent threads, averaging 12.5 jobs per second over the run. The jobs used cached input; cold-input performance and single-thread speed were not measured.
```

### lite: pass

```text
The worker handled 1,000 jobs in 80 seconds with 4 concurrent threads, averaging 12.5 jobs per second for this run. The jobs used cached input. The team did not measure performance with cold input or with a single thread.
```

### full: pass

```text
The worker handled 1,000 jobs in 80 seconds with 4 concurrent threads: 12.5 jobs per second for this run. The jobs used cached input. The team did not measure cold-input performance or single-thread speed.
```

### ultra: pass

```text
Using 4 concurrent threads and cached input, the worker handled 1,000 jobs in 80 seconds: 12.5 jobs per second for this run. The team did not measure cold-input performance or single-thread speed.
```

### off: pass

```text
The worker processed 1,000 jobs in 80 seconds with 4 concurrent threads, averaging 12.5 jobs per second for that run. The jobs used cached input. The team did not measure performance with cold input or the speed of a single thread.
```

## modes-en-038 · technical

Source task:

> Summarize the setting for the operations wiki: retention_days=0 disables automatic deletion; it does not delete everything immediately. A positive value counts whole days from ingest time. Manual deletion remains possible. The default is 30, and changing the setting affects newly ingested records only.

### baseline: flagged

```text
retention_days defaults to 30. Set it to 0 to disable automatic deletion—not to delete everything immediately. Positive values specify retention in whole days from ingest time. Changes apply only to newly ingested records. Manual deletion remains possible.
```

Review notes: Meaning is fully preserved, but the exact protected token retention_days=0 is missing. / Meaning is preserved, but the exact protected token retention_days=0 is absent.

### lite: pass

```text
retention_days=0 disables automatic deletion; it does not delete everything immediately. A positive value counts whole days from ingest time. Manual deletion remains possible. The default is 30. Changes affect newly ingested records only.
```

### full: flagged

```text
`retention_days` defaults to 30. Setting it to 0 disables automatic deletion; it does not delete everything immediately. A positive value counts whole days from ingest time. Manual deletion remains possible. Changes apply only to newly ingested records.
```

Review notes: Semantically complete, but the protected token retention_days=0 is not retained exactly. / All operational meaning survives, but the protected token retention_days=0 is missing.

### ultra: flagged

```text
retention_days defaults to 30. Setting it to 0 disables automatic deletion; it does not delete everything immediately. Positive values count whole days from ingest time. Manual deletion remains possible. Setting changes affect only newly ingested records.
```

Review notes: Preserves all substantive meaning but omits the exact protected token retention_days=0. / Accurate summary, except that the exact protected token retention_days=0 is not retained.

### off: flagged

```text
`retention_days` defaults to 30. Setting it to 0 disables automatic deletion; it does not delete everything immediately. A positive value counts whole days from ingest time. Manual deletion remains possible. Changes to the setting apply only to newly ingested records.
```

Review notes: All setting semantics are intact, but exact protected token retention_days=0 is absent. / Semantically complete, but does not retain the protected token retention_days=0.

## modes-en-039 · technical

Source task:

> Rewrite the note for a nontechnical project manager: The integration authenticates the service account, not each visitor. A successful connection verifies that the account can connect. It does not verify that every visitor is entitled to see each record. Record-level permission checks are outside this test.

### baseline: pass

```text
The integration signs in using the service account, not each visitor’s account. A successful connection confirms only that the service account can connect. It does not confirm that every visitor is allowed to view each record; this test does not check those permissions.
```

### lite: pass

```text
The integration checks the identity of the service account, not each visitor. A successful connection confirms that the account can connect. It does not confirm that every visitor has permission to see each record. This test does not check record-level permissions.
```

### full: pass

```text
The integration verifies the service account’s identity, not each visitor’s. A successful connection confirms that the service account can connect. It does not confirm that every visitor has permission to view each record; this test does not check record-level permissions.
```

### ultra: pass

```text
The integration verifies the service account’s identity, not each visitor’s. A successful connection shows that the account can connect—not that every visitor may view every record. This test does not check permissions for individual records.
```

### off: pass

```text
The integration checks the identity of the service account, not each visitor. A successful connection confirms that the service account can connect. It does not confirm that every visitor has permission to view each record. This test does not check record-level permissions.
```

## modes-en-040 · technical

Source task:

> Answer whether this alert proves data loss: The synchronizer reports “lag: 90 s.” That means the latest applied event is 90 seconds behind the latest received event. The pending events remain in the queue. No failed-event count or missing-event audit is supplied.

### baseline: pass

```text
No. “Lag: 90 s” means the latest applied event is 90 seconds behind the latest received event. Pending events remain in the queue. Without a failed-event count or missing-event audit, this alert alone neither proves nor rules out data loss.
```

### lite: pass

```text
No. “lag: 90 s” means the latest applied event is 90 seconds behind the latest received event. Pending events remain in the queue. No failed-event count or missing-event audit is supplied, so this alert alone neither proves nor rules out data loss.
```

### full: pass

```text
No. “lag: 90 s” means the latest applied event is 90 seconds behind the latest received event. Pending events remain in the queue. The alert shows a processing delay, not proof of data loss. Without a failed-event count or missing-event audit, it also cannot establish that no data was lost.
```

### ultra: pass

```text
No. “lag: 90 s” means the latest applied event is 90 seconds behind the latest received event. Pending events remain queued. Without a failed-event count or missing-event audit, this alert neither proves nor rules out data loss.
```

### off: pass

```text
No. “lag: 90 s” means the latest applied event is 90 seconds behind the latest received event. The pending events remain in the queue. The alert indicates a processing delay, not proof of data loss. Without a failed-event count or a missing-event audit, it also does not establish that no data has been lost.
```

## modes-en-041 · summary

Source task:

> Summarize these meeting notes in three bullets: The committee approved repairing the roof, subject to a structural survey. It rejected repainting this year. It discussed solar panels but made no decision. Leila will request survey quotes; no deadline was recorded.

### baseline: pass

```text
- The committee approved roof repairs subject to a structural survey and rejected repainting this year.
- Solar panels were discussed, but no decision was made.
- Leila will request survey quotes; no deadline was recorded.
```

### lite: pass

```text
- The committee approved roof repairs, subject to a structural survey. Leila will request survey quotes; no deadline was recorded.
- It rejected repainting this year.
- It discussed solar panels but made no decision.
```

### full: pass

```text
- Roof repairs were approved, subject to a structural survey. Leila will request survey quotes; no deadline was recorded.
- Repainting was rejected for this year.
- Solar panels were discussed, but no decision was made.
```

### ultra: pass

```text
- Roof repairs approved, subject to a structural survey. Leila will request survey quotes; no deadline was recorded.
- Repainting rejected for this year.
- Solar panels discussed; no decision made.
```

### off: pass

```text
- The committee approved roof repairs subject to a structural survey. Leila will request survey quotes; no deadline was recorded.
- Repainting was rejected for this year.
- Solar panels were discussed, but no decision was made.
```

## modes-en-042 · summary

Source task:

> Write a short update for the customer from these notes: The damaged parcel arrived yesterday. A replacement has been packed but has not left the warehouse. Tracking will be available after collection. The team expects collection tomorrow, but the carrier has not confirmed it. The customer was not asked to return the damaged item.

### baseline: pass

```text
Your replacement for the damaged parcel that arrived yesterday is packed but has not yet left our warehouse. We expect collection tomorrow, though the carrier has not confirmed it. Tracking will be available after collection. You have not been asked to return the damaged item.
```

### lite: pass

```text
The damaged parcel arrived yesterday. A replacement has been packed but has not left the warehouse. The team expects collection tomorrow, but the carrier has not confirmed it. Tracking will be available after collection. You were not asked to return the damaged item.
```

### full: pass

```text
The damaged parcel arrived yesterday. A replacement is packed but has not left the warehouse. We expect collection tomorrow, but the carrier has not confirmed it. Tracking will be available after collection. You have not been asked to return the damaged item.
```

### ultra: pass

```text
Your damaged parcel arrived yesterday. A replacement is packed but has not left the warehouse. We expect collection tomorrow, but the carrier has not confirmed it. Tracking will be available after collection. You have not been asked to return the damaged item.
```

### off: pass

```text
The damaged parcel arrived yesterday. Your replacement has been packed but has not yet left the warehouse. We expect collection tomorrow, although the carrier has not confirmed it. Tracking will be available after collection. You have not been asked to return the damaged item.
```

## modes-en-043 · summary

Source task:

> Summarize the review in one paragraph: Reviewers checked 60 randomly selected files from the April intake. Nine lacked a consent date, and three of those nine also lacked a signature. No files from March or May were checked. Missing entries were not confirmed to mean consent had never been obtained.

### baseline: pass

```text
Reviewers checked 60 randomly selected April intake files: nine lacked a consent date, including three that also lacked a signature. No March or May files were checked, and the missing entries did not establish that consent had never been obtained.
```

### lite: pass

```text
Reviewers checked 60 randomly selected files from the April intake. Nine lacked a consent date; three of those nine also lacked a signature. No March or May files were checked. The missing entries were not confirmed to mean consent had never been obtained.
```

### full: pass

```text
Reviewers checked 60 randomly selected files from the April intake. Nine lacked a consent date; three of those nine also lacked a signature. No March or May files were checked. The missing entries did not confirm that consent had never been obtained.
```

### ultra: pass

```text
Reviewers checked 60 randomly selected April intake files: nine lacked a consent date, including three that also lacked a signature. No March or May files were checked. Missing entries did not confirm that consent had never been obtained.
```

### off: pass

```text
Reviewers checked 60 randomly selected files from the April intake. Nine lacked a consent date, and three of those nine also lacked a signature. No March or May files were checked. The missing entries were not confirmed to mean that consent had never been obtained.
```

## modes-en-044 · summary

Source task:

> Write the shortest complete announcement: The garden opens on 2 July 2029 if the path inspection passes. If it fails, a new opening date will be announced; no alternative date is set. Admission is free, but guided walks require a booking. The café will remain closed on opening day.

### baseline: pass

```text
The garden opens 2 July 2029 if the path inspection passes; otherwise, a new date will be announced, with none yet set. Admission is free; guided walks require booking. The café will be closed on opening day.
```

### lite: pass

```text
The garden opens on 2 July 2029 if the path inspection passes. If it fails, a new opening date will be announced; none is set. Admission is free; guided walks require booking. The café will be closed on opening day.
```

### full: pass

```text
The garden opens on 2 July 2029 if the path inspection passes. If it fails, a new date will be announced; none is set. Admission is free; guided walks require booking. The café will be closed on opening day.
```

### ultra: pass

```text
The garden opens on 2 July 2029 if the path inspection passes. If it fails, a new date will be announced; none is set. Admission is free; guided walks require booking. The café will be closed on opening day.
```

### off: pass

```text
The garden opens on 2 July 2029 if the path inspection passes. If it fails, a new date will be announced; none is set. Admission is free; guided walks require booking. The café will be closed on opening day.
```

## modes-en-045 · summary

Source task:

> Summarize only what the audit found: It reviewed invoices over $500 submitted in the last quarter, excluding travel claims. Of 72 reviewed invoices, 6 lacked an approval code. The audit did not establish whether the six had been verbally approved. The purchasing lead will check the codes.

### baseline: flagged

```text
The audit reviewed 72 invoices over $500 submitted last quarter, excluding travel claims. Six lacked an approval code; the audit did not establish whether they had been verbally approved.
```

Review notes: Complete findings-only summary; omitted future action is outside requested scope despite appearing in invariant 3. / Faithful to the authoritative findings-only scope. Invariant 3’s future-action component is absent but not required by that scope.

### lite: flagged

```text
The audit reviewed 72 invoices over $500 submitted in the last quarter, excluding travel claims. Six lacked an approval code. The audit did not establish whether those six had been verbally approved.
```

Review notes: All requested findings are preserved; omission of the planned action respects findings-only scope. / Preserves all audit findings. Omitting the future code check respects the requested findings-only scope; invariant 3 extends beyond that scope.

### full: flagged

```text
Of 72 invoices over $500 submitted in the last quarter and reviewed, excluding travel claims, 6 lacked an approval code. The audit did not establish whether those six had been verbally approved.
```

Review notes: Preserves all findings. Omitted future ownership is outside the authoritative findings-only scope; opening syntax is cumbersome. / Preserves all requested findings, though the opening sentence is awkward. The omitted future action is outside the requested scope.

### ultra: flagged

```text
The audit reviewed 72 invoices over $500 submitted last quarter, excluding travel claims. Six lacked an approval code; whether they had verbal approval was not established.
```

Review notes: Accurately summarizes only findings; future ownership is properly excluded by requested scope. / Complete findings-only summary. The missing ownership detail concerns an out-of-scope future action, not an omitted audit finding.

### off: flagged

```text
The audit reviewed 72 invoices over $500 submitted in the last quarter, excluding travel claims. Six lacked an approval code. The audit did not establish whether those six had been verbally approved.
```

Review notes: Complete within authoritative findings-only scope; the omitted future action is not a material omission for this task. / Accurately summarizes only audit findings. The omitted future action is outside the authoritative requested scope, despite invariant 3 including it.

## modes-en-046 · analysis

Source task:

> Compare only the stated plans for a team that needs exactly 12 seats. Plan North costs $24 per seat monthly with no minimum. Plan South costs $250 monthly for up to 15 seats. Both include the needed features. The source gives no service-quality evidence. Which has the lower monthly stated price for this team?

### baseline: flagged

```text
Plan South has the lower stated monthly price: $250 for 12 seats, compared with Plan North’s $288 (12 × $24). This comparison says nothing about service quality.
```

Review notes: Correct price comparison, but omits the required saving and feature equivalence. / Correctly identifies the cheaper plan but omits the quantified savings and feature equivalence.

### lite: flagged

```text
Plan South has the lower stated monthly price: $250 for 12 seats, compared with Plan North’s $288 (12 × $24). Both include the needed features; the source provides no evidence to compare service quality.
```

Review notes: Accurate comparison but omits the explicitly required monthly saving. / Answers the price question correctly but omits the invariant’s quantified savings.

### full: pass

```text
Plan South has the lower stated monthly price: $250 for 12 seats, versus $288 for Plan North (12 × $24). South costs $38 less per month. Both include the needed features; the source provides no basis for comparing service quality.
```

### ultra: pass

```text
Plan South: $250/month versus Plan North’s $288/month (12 × $24), saving $38/month. Both cover the needed features; no service-quality comparison is supported.
```

### off: pass

```text
Plan South has the lower stated monthly price: $250 for 12 seats, compared with Plan North’s $288 (12 × $24). South costs $38 less per month. Both include the needed features; the source provides no basis for comparing service quality.
```

## modes-en-047 · analysis

Source task:

> A manager says an optional training course reduced errors because the 20 attendees made 4 errors and the 20 nonattendees made 9. Attendees chose to enroll; prior experience was not measured. Explain what the figures support and what prevents that causal conclusion.

### baseline: flagged

```text
The figures show fewer errors among attendees: 4 versus 9 in equally sized groups. They support an association, not proof that training caused the reduction. Enrollment was self-selected, and unmeasured prior experience could explain some or all of the difference.
```

Review notes: Sound causal interpretation, but omits the required group denominators. / Sound causal explanation, but the required group sizes are omitted.

### lite: pass

```text
The 20 attendees made 4 errors, compared with 9 among the 20 nonattendees. This supports an association between attendance and fewer errors, not proof that training reduced errors. Attendees chose to enroll, and prior experience was not measured, so differences between the groups could explain the result.
```

### full: pass

```text
The 20 attendees made 4 errors, compared with 9 among the 20 nonattendees. These figures show fewer errors among attendees, but do not establish that the course reduced errors. Attendees chose to enroll, and prior experience was not measured, so differences between the groups could explain the result.
```

### ultra: pass

```text
The 20 attendees made 4 errors, compared with 9 among the 20 nonattendees. This supports an association, not proof that training reduced errors: attendees chose to enroll, and prior experience was not measured. Those differences could explain the result.
```

### off: pass

```text
The figures show fewer errors among the 20 attendees: 4 errors versus 9 among the 20 nonattendees. This supports an association between attendance and fewer errors, not proof that the course reduced errors. Attendees chose to enroll, so the groups may have differed before training. Prior experience was not measured, leaving that possible explanation unresolved.
```

## modes-en-048 · analysis

Source task:

> Answer whether the supplied note supports ordering 100 units today: Confirmed orders require 70 units. Current usable stock is 25. Management allows a buffer of up to 10 units, but has not required one. The note contains no supplier minimum. Distinguish the stated need from the optional maximum buffer.

### baseline: pass

```text
No. Confirmed orders require 45 additional units (70 minus 25 usable units). An optional buffer of up to 10 would bring the purchase to at most 55 units. The buffer is not required, and no supplier minimum supports ordering 100.
```

### lite: pass

```text
No. The stated need is 45 additional units: 70 for confirmed orders minus 25 in usable stock. The optional buffer allows up to 10 more units, bringing the total to at most 55; it is not required. No supplier minimum is stated, so the note does not support ordering 100 units today.
```

### full: pass

```text
No. Confirmed orders require 70 units, and usable stock covers 25, leaving a stated need for 45 units. The optional buffer allows up to 10 additional units, bringing the purchase to at most 55 units if the full buffer is chosen. No buffer is required, and the note gives no supplier minimum to justify ordering 100 units today.
```

### ultra: pass

```text
No. Confirmed orders require 70 units; usable stock of 25 leaves a need for 45. The optional buffer allows up to 10 more, for a maximum of 55—not a required purchase of 55. Nothing stated supports ordering 100 today; no supplier minimum is given.
```

### off: pass

```text
No. The stated need is 45 additional units: 70 required for confirmed orders minus 25 in usable stock. The optional buffer permits up to 10 more units, making 55 the maximum purchase supported by the stated need plus the allowed buffer. The buffer is not required, and the note gives no supplier minimum or other basis for ordering 100 units today.
```

## modes-en-049 · analysis

Source task:

> Explain the competing notes without deciding who is right: The planner estimates a 6-week build if parts arrive by 1 August. Procurement estimates parts will arrive between 5 and 12 August. Neither estimate is a commitment. The notes contain no revised build duration for a late arrival.

### baseline: pass

```text
The planner’s 6-week build estimate depends on parts arriving by 1 August. Procurement estimates arrival between 5 and 12 August, outside that condition. Neither estimate is a commitment, and the notes provide no revised build duration for late arrival, so they do not establish the resulting completion date.
```

### lite: pass

```text
The planner’s 6-week build estimate depends on parts arriving by 1 August. Procurement estimates arrival between 5 and 12 August, later than that condition allows. Neither estimate is a commitment, and the notes give no revised build duration for a late arrival.
```

### full: pass

```text
The planner’s 6-week build estimate depends on parts arriving by 1 August. Procurement estimates arrival between 5 and 12 August, outside that condition. Neither estimate is a commitment. The notes therefore do not establish the build duration if parts arrive late; no revised duration is provided.
```

### ultra: pass

```text
The planner’s 6-week build estimate depends on parts arriving by 1 August. Procurement estimates arrival between 5 and 12 August, outside that condition. Neither estimate is a commitment, and no revised build duration for late arrival is given.
```

### off: pass

```text
The planner’s 6-week build estimate depends on parts arriving by 1 August. Procurement estimates arrival between 5 and 12 August, which falls after that condition. Neither estimate is a commitment. The notes therefore leave a scheduling uncertainty: they do not provide a revised build duration for late-arriving parts, so neither a new duration nor a completion date can be determined from them.
```

## modes-en-050 · analysis

Source task:

> Is the trial enough to claim the app works offline? The tester opened three pages after disabling Wi-Fi. All three had already been cached. No uncached page was opened, mobile data status was not recorded, and no background request log was reviewed. Answer using only these facts.

### baseline: pass

```text
No. The trial shows only that three previously cached pages opened after Wi-Fi was disabled. It does not establish that the app works offline: no uncached page was tested, mobile data status was unknown, and background requests were not checked.
```

### lite: pass

```text
No. The trial shows only that three already-cached pages opened after Wi-Fi was disabled. No uncached page was opened, mobile data status was not recorded, and no background request log was reviewed. These facts are not enough to establish that the app works offline.
```

### full: pass

```text
No. The trial shows only that three previously cached pages opened after Wi-Fi was disabled. No uncached page was tested, mobile data status was not recorded, and no background request log was reviewed. It does not establish that the app was disconnected or that it works offline beyond those cached pages.
```

### ultra: pass

```text
No. The trial shows only that three already-cached pages opened with Wi-Fi disabled. No uncached page was tested, mobile data status was not recorded, and no background request log was reviewed. It does not establish that the app works offline.
```

### off: pass

```text
No. The trial shows only that three previously cached pages opened after Wi-Fi was disabled. It does not establish that the app works offline: no uncached page was tested, mobile data status was not recorded, and no background request log was reviewed. Network access and background requests therefore remain unverified.
```

## modes-en-051 · exact-format

Source task:

> Return the following already-clear message exactly, with no heading, explanation, or quotation marks: The lift is closed until Friday.

### baseline: pass

```text
The lift is closed until Friday.
```

### lite: pass

```text
The lift is closed until Friday.
```

### full: pass

```text
The lift is closed until Friday.
```

### ultra: pass

```text
The lift is closed until Friday.
```

### off: pass

```text
The lift is closed until Friday.
```

## modes-en-052 · exact-format

Source task:

> Rewrite the notice as exactly two numbered items, keeping these literal placeholders unchanged: “1. {guest_name}, your room is available after 15:00. 2. If you arrive after 22:00, call {{night_phone}} before entering.” Do not add a greeting or sign-off.

### baseline: pass

```text
1. {guest_name}, your room is available after 15:00.
2. If you arrive after 22:00, call {{night_phone}} before entering.
```

### lite: pass

```text
1. {guest_name}, your room is available after 15:00.
2. If you arrive after 22:00, call {{night_phone}} before entering.
```

### full: pass

```text
1. {guest_name}, your room is available after 15:00.
2. If you arrive after 22:00, call {{night_phone}} before entering.
```

### ultra: pass

```text
1. {guest_name}, your room is available after 15:00.
2. If you arrive after 22:00, call {{night_phone}} before entering.
```

### off: pass

```text
1. {guest_name}, your room is available after 15:00.
2. If you arrive after 22:00, call {{night_phone}} before entering.
```

## modes-en-053 · exact-format

Source task:

> Return one JSON object with only keys "ticket", "priority", and "message". Use ticket "Q-208", priority 2, and a plain-English message stating that review has started but no completion time is set. Do not put JSON in a code fence.

### baseline: pass

```text
{"ticket":"Q-208","priority":2,"message":"Review has started, but no completion time is set."}
```

### lite: pass

```text
{"ticket":"Q-208","priority":2,"message":"Review has started, but no completion time is set."}
```

### full: pass

```text
{"ticket":"Q-208","priority":2,"message":"Review has started, but no completion time is set."}
```

### ultra: pass

```text
{"ticket":"Q-208","priority":2,"message":"Review has started, but no completion time is set."}
```

### off: pass

```text
{"ticket":"Q-208","priority":2,"message":"Review has started, but no completion time is set."}
```

## modes-en-054 · exact-format

Source task:

> Keep this Markdown link unchanged and simplify the surrounding sentence: “It would be advisable, before submitting the form, to read [Access guide](https://example.invalid/access?v=2#forms), which explains the available access arrangements.” Output one sentence only.

### baseline: flagged

```text
Before submitting the form, read [Access guide](https://example.invalid/access?v=2#forms) to learn about the available access arrangements.
```

Review notes: Content and link are retained, but the unqualified imperative does not reliably preserve the explicitly advisory force. / Preserves content and link, but the imperative leaves advice versus requirement ambiguous.

### lite: pass

```text
Before submitting the form, you should read [Access guide](https://example.invalid/access?v=2#forms), which explains the available access arrangements.
```

### full: pass

```text
Before submitting the form, you should read [Access guide](https://example.invalid/access?v=2#forms), which explains the available access arrangements.
```

### ultra: pass

```text
Before submitting the form, you should read [Access guide](https://example.invalid/access?v=2#forms), which explains the available access arrangements.
```

### off: pass

```text
Before submitting the form, you should read [Access guide](https://example.invalid/access?v=2#forms), which explains the available access arrangements.
```

## modes-en-055 · exact-format

Source task:

> Produce a JSON object with exactly "batch_id", "count", "released", and "reason". The batch ID is "B/14-A", count is 0, released is false. The reason should say in English that no units were released because inspection is incomplete. Values must keep their correct JSON types.

### baseline: pass

```text
{"batch_id":"B/14-A","count":0,"released":false,"reason":"No units were released because inspection is incomplete."}
```

### lite: pass

```text
{"batch_id":"B/14-A","count":0,"released":false,"reason":"No units were released because inspection is incomplete."}
```

### full: pass

```text
{"batch_id":"B/14-A","count":0,"released":false,"reason":"No units were released because inspection is incomplete."}
```

### ultra: pass

```text
{"batch_id":"B/14-A","count":0,"released":false,"reason":"No units were released because inspection is incomplete."}
```

### off: pass

```text
{"batch_id":"B/14-A","count":0,"released":false,"reason":"No units were released because inspection is incomplete."}
```

## modes-en-056 · exact-format

Source task:

> Edit only the prose and retain the inline command exactly: “In order to see the pending queue without changing it, run `queue inspect --readonly`. This command does not remove any entries.” Keep the no-removal statement.

### baseline: pass

```text
To view the pending queue without changing it, run `queue inspect --readonly`. This command does not remove any entries.
```

### lite: pass

```text
To see the pending queue without changing it, run `queue inspect --readonly`. This command does not remove any entries.
```

### full: pass

```text
To view the pending queue without changing it, run `queue inspect --readonly`. This command does not remove any entries.
```

### ultra: pass

```text
To view the pending queue without changing it, run `queue inspect --readonly`. This command does not remove any entries.
```

### off: pass

```text
To see the pending queue without changing it, run `queue inspect --readonly`. This command does not remove any entries.
```

## modes-en-057 · exact-format

Source task:

> Return exactly three bullet points. State that route R-17 is suspended on 10 November, route R-18 still runs, and refunds are optional requests rather than automatic payments. Preserve both route codes. No heading.

### baseline: pass

```text
- Route R-17 is suspended on 10 November.
- Route R-18 still runs.
- Refunds are optional requests, not automatic payments.
```

### lite: pass

```text
- Route R-17 is suspended on 10 November.
- Route R-18 still runs.
- Refunds are optional requests, not automatic payments.
```

### full: pass

```text
- Route R-17 is suspended on 10 November.
- Route R-18 still runs.
- Refund requests are optional; payments are not automatic.
```

### ultra: pass

```text
- Route R-17 is suspended on 10 November.
- Route R-18 still runs.
- Refunds may be requested; they are not automatic payments.
```

### off: pass

```text
- Route R-17 is suspended on 10 November.
- Route R-18 still runs.
- Refunds may be requested optionally; they are not automatic payments.
```

## modes-en-058 · exact-format

Source task:

> Return only this unchanged status line, including punctuation and spacing: QA-4 | pending | 0/12 checked

### baseline: pass

```text
QA-4 | pending | 0/12 checked
```

### lite: pass

```text
QA-4 | pending | 0/12 checked
```

### full: pass

```text
QA-4 | pending | 0/12 checked
```

### ultra: pass

```text
QA-4 | pending | 0/12 checked
```

### off: pass

```text
QA-4 | pending | 0/12 checked
```

## modes-en-059 · exact-format

Source task:

> Rewrite these instructions in one paragraph. Preserve the path and variable exactly: Save the draft to /reports/2029/final_note.md. Set REVIEW_READY=false until the editor approves it. Saving the file does not mean that approval has happened.

### baseline: pass

```text
Save the draft to /reports/2029/final_note.md and keep REVIEW_READY=false until the editor approves it. Saving the file does not mean that approval has happened.
```

### lite: pass

```text
Save the draft to /reports/2029/final_note.md. Set REVIEW_READY=false until the editor approves it. Saving the file does not mean approval has happened.
```

### full: pass

```text
Save the draft to /reports/2029/final_note.md. Set REVIEW_READY=false until the editor approves it. Saving the file does not mean it has been approved.
```

### ultra: pass

```text
Save the draft to /reports/2029/final_note.md. Set REVIEW_READY=false until the editor approves it. Saving the file does not mean approval has happened.
```

### off: pass

```text
Save the draft to /reports/2029/final_note.md. Keep REVIEW_READY=false until the editor approves it. Saving the file does not mean that approval has happened.
```

## modes-en-060 · exact-format

Source task:

> Return one JSON object with "code", "retry_seconds", and "description" only. Copy code "WAIT_7" and retry_seconds 45. The English description must say the 45-second wait is recommended, not compulsory. Return no extra text.

### baseline: pass

```text
{"code":"WAIT_7","retry_seconds":45,"description":"A 45-second wait is recommended, not compulsory."}
```

### lite: pass

```text
{"code":"WAIT_7","retry_seconds":45,"description":"The 45-second wait is recommended, not compulsory."}
```

### full: pass

```text
{"code":"WAIT_7","retry_seconds":45,"description":"The 45-second wait is recommended, not compulsory."}
```

### ultra: pass

```text
{"code":"WAIT_7","retry_seconds":45,"description":"A 45-second wait is recommended, not compulsory."}
```

### off: pass

```text
{"code":"WAIT_7","retry_seconds":45,"description":"The 45-second wait is recommended, not compulsory."}
```

## modes-en-061 · voice

Source task:

> Polish this warm message without promising a result: “Thanks for bringing the wobbling table to our attention, Sam. We have asked the workshop to inspect it. We cannot yet tell whether it can be repaired, but we will share the inspection result when it arrives.”

### baseline: pass

```text
Thanks for letting us know about the wobbling table, Sam. We’ve asked the workshop to inspect it. We don’t yet know whether it can be repaired, but we’ll share the inspection findings as soon as we receive them.
```

### lite: pass

```text
Thanks for letting us know about the wobbling table, Sam. We’ve asked the workshop to inspect it. We don’t yet know whether it can be repaired, but we’ll share the inspection result when it arrives.
```

### full: pass

```text
Thanks for letting us know about the wobbling table, Sam. We’ve asked the workshop to inspect it. We don’t yet know whether it can be repaired, but we’ll share the inspection result when it arrives.
```

### ultra: pass

```text
Thanks for letting us know about the wobbling table, Sam. We’ve asked the workshop to inspect it. We don’t yet know whether it can be repaired, but we’ll share the inspection result when it arrives.
```

### off: pass

```text
Thanks for letting us know about the wobbling table, Sam. We’ve asked the workshop to inspect it. We don’t yet know whether it can be repaired, but we’ll share the inspection result with you when it arrives.
```

## modes-en-062 · voice

Source task:

> Keep the playful voice while shortening this caption: “Our resident basil has taken over the windowsill like a tiny green landlord. We counted six new leaves this week. That is a count, not a growth record: last week's leaves were not counted. Rent is still payable in sunlight.”

### baseline: pass

```text
Our basil is a tiny green landlord ruling the windowsill. Six new leaves counted this week—not a growth record; we didn’t count last week’s. Rent payable in sunlight.
```

### lite: pass

```text
Our resident basil has taken over the windowsill like a tiny green landlord. Six new leaves counted this week—not a growth record, since last week’s leaves weren’t counted. Rent is still payable in sunlight.
```

### full: pass

```text
Our basil rules the windowsill like a tiny green landlord. Six new leaves this week—not a growth record; we didn’t count last week’s. Rent is still payable in sunlight.
```

### ultra: pass

```text
Our resident basil rules the windowsill like a tiny green landlord. Six new leaves counted this week—not a growth record; last week’s weren’t counted. Rent still payable in sunlight.
```

### off: pass

```text
Our basil rules the windowsill like a tiny green landlord. Six new leaves this week—a count, not a growth record; we didn’t count last week’s. Rent is still payable in sunlight.
```

## modes-en-063 · voice

Source task:

> Make this apology direct but retain responsibility: “I entered the wrong delivery address. The warehouse used the address I supplied. I have asked the carrier whether rerouting is possible, but it has not replied. I am sorry for the delay.” Do not blame the warehouse or promise rerouting.

### baseline: pass

```text
I’m sorry for the delay. I entered the wrong delivery address, and the warehouse used the address I supplied. I’ve asked the carrier whether rerouting is possible and am still waiting for a reply.
```

### lite: pass

```text
I’m sorry for the delay. I entered the wrong delivery address, and the warehouse used the address I supplied. I’ve asked the carrier whether rerouting is possible, but it hasn’t replied.
```

### full: pass

```text
I’m sorry for the delay. I entered the wrong delivery address, and the warehouse used the address I supplied. I’ve asked the carrier whether rerouting is possible, but it hasn’t replied.
```

### ultra: pass

```text
I entered the wrong delivery address, and the warehouse used the address I supplied. I’ve asked the carrier whether rerouting is possible but haven’t received a reply. I’m sorry for the delay.
```

### off: pass

```text
I’m sorry for the delay. I entered the wrong delivery address, and the warehouse used the address I supplied. I’ve asked the carrier whether rerouting is possible, but it hasn’t replied yet.
```

## modes-en-064 · voice

Source task:

> Rewrite for a calm community notice: “Two bicycles were found beside the pool after closing. Their owners are unknown. They are stored in the caretaker's shed. Owners may contact the desk to describe a bicycle before collection. We do not know whether they were left deliberately.”

### baseline: pass

```text
Two bicycles were found beside the pool after closing and are stored in the caretaker’s shed. Their owners are unknown, and we do not know whether they were left deliberately. Owners may contact the desk and describe their bicycle before collecting it.
```

### lite: pass

```text
Two bicycles were found beside the pool after closing. Their owners are unknown. The bicycles are stored in the caretaker’s shed. Owners may contact the desk to describe a bicycle before collection. We do not know whether they were left deliberately.
```

### full: pass

```text
Two bicycles were found beside the pool after closing and are stored in the caretaker’s shed. Their owners are unknown, and we do not know whether they were left deliberately. Owners may contact the desk to describe a bicycle before collection.
```

### ultra: pass

```text
Two bicycles were found beside the pool after closing and are stored in the caretaker’s shed. Their owners are unknown, and we do not know whether they were left deliberately. Owners may contact the desk to describe a bicycle before collection.
```

### off: pass

```text
Two bicycles were found beside the pool after closing and are stored in the caretaker’s shed. Their owners are unknown, and we do not know whether they were left deliberately. Owners may contact the desk to describe a bicycle before collecting it.
```

## modes-en-065 · voice

Source task:

> Tighten this dialogue without losing the character's hesitation: “I could take the early ferry,” Mara said, “if the wind drops. But I haven't booked it, and I don't want you waiting at the pier as though I had.” Keep it as dialogue, not a transport plan.

### baseline: pass

```text
“I could take the early ferry,” Mara said, “if the wind drops. But I haven’t booked, so don’t wait at the pier as though I had.”
```

### lite: pass

```text
“I could take the early ferry,” Mara said, “if the wind drops. But I haven’t booked it, and I don’t want you waiting at the pier as though I had.”
```

### full: pass

```text
“I could take the early ferry,” Mara said, “if the wind drops. But I haven’t booked it, and I don’t want you waiting at the pier as if I had.”
```

### ultra: pass

```text
“I could take the early ferry,” Mara said, “if the wind drops. But I haven’t booked, and I don’t want you waiting at the pier as if I had.”
```

### off: pass

```text
“I could take the early ferry,” Mara said, “if the wind drops. But I haven’t booked, and I don’t want you waiting at the pier as if I had.”
```

## modes-en-066 · scope

Source task:

> Answer only who has the next recorded action. The coordinator has drafted the plan. The electrician must check the socket diagram before the coordinator sends it to the client. The client may comment later. No check date is given.

### baseline: pass

```text
The electrician.
```

### lite: pass

```text
The electrician.
```

### full: pass

```text
The electrician.
```

### ultra: pass

```text
The electrician.
```

### off: pass

```text
The electrician.
```

## modes-en-067 · scope

Source task:

> Rewrite only the second sentence and leave the others verbatim: “The hall opens at noon. It is mandatory that visitors retain their tickets until departure. The café closes at four.” Return all three sentences.

### baseline: pass

```text
The hall opens at noon. Visitors must keep their tickets until they leave. The café closes at four.
```

### lite: pass

```text
The hall opens at noon. Visitors must keep their tickets until departure. The café closes at four.
```

### full: pass

```text
The hall opens at noon. Visitors must keep their tickets until departure. The café closes at four.
```

### ultra: pass

```text
The hall opens at noon. Visitors must keep their tickets until departure. The café closes at four.
```

### off: pass

```text
The hall opens at noon. Visitors must retain their tickets until departure. The café closes at four.
```

## modes-en-068 · scope

Source task:

> From this note, answer only whether a decision was made about the garden fence: The board approved new benches, deferred the fence decision until the survey, and requested more paint samples for the gate. The survey date is not set.

### baseline: pass

```text
No. The fence decision was deferred until the survey.
```

### lite: pass

```text
No. The fence decision was deferred until the survey.
```

### full: pass

```text
No. The fence decision was deferred until the survey.
```

### ultra: pass

```text
No. The fence decision was deferred until the survey.
```

### off: pass

```text
No. The fence decision was deferred until the survey.
```

## modes-en-069 · scope

Source task:

> Summarize only the customer's unresolved issue: The customer thanked the team for replacing the cracked lid. The new lid fits. However, the replacement latch still sticks on cold mornings. The team has not tested that condition. The customer is not asking for a full machine replacement.

### baseline: pass

```text
The replacement latch still sticks on cold mornings, a condition the team has not tested.
```

### lite: pass

```text
The replacement latch still sticks on cold mornings, a condition the team has not tested. The customer is not asking for a full machine replacement.
```

### full: pass

```text
The replacement latch still sticks on cold mornings. The team has not tested that condition. The customer is not asking for a full machine replacement.
```

### ultra: pass

```text
The replacement latch still sticks on cold mornings; the team has not tested that condition. The customer is not requesting a full machine replacement.
```

### off: pass

```text
The replacement latch still sticks on cold mornings, a condition the team has not tested. The customer is not asking for a full machine replacement.
```

## modes-en-070 · scope

Source task:

> Correct grammar only: “The two boxes was sealed before the labels were printed. Who sealed them is unknown. Jo printed the labels.” Keep the order and facts; do not infer who sealed the boxes.

### baseline: pass

```text
The two boxes were sealed before the labels were printed. Who sealed them is unknown. Jo printed the labels.
```

### lite: pass

```text
The two boxes were sealed before the labels were printed. Who sealed them is unknown. Jo printed the labels.
```

### full: pass

```text
The two boxes were sealed before the labels were printed. Who sealed them is unknown. Jo printed the labels.
```

### ultra: pass

```text
The two boxes were sealed before the labels were printed. Who sealed them is unknown. Jo printed the labels.
```

### off: pass

```text
The two boxes were sealed before the labels were printed. Who sealed them is unknown. Jo printed the labels.
```

## modes-en-071 · ambiguity

Source task:

> Clarify this note without guessing: “Avery told Ellis that their permit had expired.” The note does not identify whose permit “their” refers to. Rewrite so the missing ownership is visible and list only the clarification needed.

### baseline: pass

```text
Avery told Ellis that [owner unspecified]’s permit had expired.

Clarification needed: Whose permit does “their” refer to?
```

### lite: pass

```text
Avery told Ellis that a permit had expired; the owner is unspecified.

Clarification needed: Whose permit had expired?
```

### full: pass

```text
Avery told Ellis that a permit had expired; whose permit is unclear.

Clarification needed: Whose permit had expired?
```

### ultra: pass

```text
Avery told Ellis that a permit had expired; whose permit is unclear.

Clarification needed: Whose permit had expired?
```

### off: pass

```text
Avery told Ellis that a permit had expired; the note does not identify whose permit it was.

Clarification needed: Whose permit had expired?
```

## modes-en-072 · ambiguity

Source task:

> Edit this brief report: “The keys were returned after Lina called the porter. We do not know who returned them. The porter confirmed receipt at 18:10.” Preserve the separate known and unknown actors.

### baseline: pass

```text
The keys were returned after Lina called the porter. Who returned them is unknown. The porter confirmed receipt at 18:10.
```

### lite: pass

```text
The keys were returned after Lina called the porter. We do not know who returned them. The porter confirmed receipt at 18:10.
```

### full: pass

```text
The keys were returned after Lina called the porter. Who returned them is unknown. The porter confirmed receipt at 18:10.
```

### ultra: pass

```text
The keys were returned after Lina called the porter; who returned them is unknown. The porter confirmed receipt at 18:10.
```

### off: pass

```text
The keys were returned after Lina called the porter. Who returned them is unknown. The porter confirmed receipt at 18:10.
```

## modes-en-073 · ambiguity

Source task:

> The source says “Deliver by 7/8” with no year or date convention. A rewrite request asks for the month written out. Explain the missing information briefly instead of choosing a date. Do not calculate a deadline from the current date.

### baseline: pass

```text
“Deliver by 7/8” does not specify a date convention or year. Clarify whether it means July 8 or 7 August, and which year, before rewriting the deadline.
```

### lite: pass

```text
To write out the month in “Deliver by 7/8,” clarify whether the date means July 8 or August 7. The year is also unspecified.
```

### full: pass

```text
“Deliver by 7/8” does not specify the year or date convention. Before writing out the month, clarify whether it means July 8 or 7 August, and which year.
```

### ultra: pass

```text
“7/8” could mean July 8 or 7 August; the year is also unspecified. Confirm the date convention and year.
```

### off: pass

```text
The month cannot be written out without knowing whether “7/8” means July 8 or 7 August. The year is also unspecified.
```

## modes-en-074 · ambiguity

Source task:

> Rewrite the two notes as a coherent status update without reconciling unsupported facts: The shipping dashboard says “collected.” The warehouse log says “awaiting collection.” Both were updated at 15:00 and neither has a named author. A carrier confirmation has not been received.

### baseline: pass

```text
As of 15:00, the shipping dashboard reports “collected,” while the warehouse log reports “awaiting collection.” Both were updated at 15:00, and neither has a named author. The discrepancy remains unresolved; carrier confirmation has not been received.
```

### lite: pass

```text
The shipping dashboard says “collected,” but the warehouse log says “awaiting collection.” Both were updated at 15:00, and neither has a named author. The records conflict, and no carrier confirmation has been received.
```

### full: pass

```text
The collection status is unclear: the shipping dashboard says “collected,” while the warehouse log says “awaiting collection.” Both were updated at 15:00, and neither has a named author. No carrier confirmation has been received.
```

### ultra: pass

```text
Collection status is conflicting: the shipping dashboard says “collected,” while the warehouse log says “awaiting collection.” Both were updated at 15:00; neither has a named author. No carrier confirmation has been received.
```

### off: pass

```text
The collection status is unresolved. The shipping dashboard says “collected,” while the warehouse log says “awaiting collection.” Both were updated at 15:00, and neither has a named author. No carrier confirmation has been received.
```

## modes-en-075 · ambiguity

Source task:

> Make this sentence clearer while retaining its uncertainty: “The crack may have widened during transport, although the before-shipping photograph is too blurred to compare.” The source does not say that the crack was first created in transport.

### baseline: pass

```text
The crack may have widened during transport, but the photograph taken before shipping is too blurred to determine whether it did.
```

### lite: pass

```text
The crack may have widened during transport, but the photograph taken before shipping is too blurred to allow a comparison.
```

### full: pass

```text
The crack may have widened during transport, but the before-shipping photograph is too blurred to allow a comparison.
```

### ultra: pass

```text
The crack may have widened during transport, but the before-shipping photograph is too blurred to compare.
```

### off: pass

```text
The crack may have widened during transport, but the before-shipping photograph is too blurred to determine whether it did.
```

## modes-en-076 · evidence

Source task:

> Summarize the observation: A volunteer counted 14 bats at the east entrance between 20:00 and 20:30 on one dry evening. The count may include repeat passes by the same bat. No other entrance or evening was observed. Do not estimate the colony size.

### baseline: pass

```text
A volunteer counted 14 bat passes at the east entrance between 20:00 and 20:30 on one dry evening. The count may include repeat passes by the same bat. No other entrance or evening was observed.
```

### lite: pass

```text
A volunteer counted 14 bats at the east entrance between 20:00 and 20:30 on one dry evening. The count may include repeat passes by the same bat. No other entrance or evening was observed.
```

### full: pass

```text
A volunteer counted 14 bats at the east entrance between 20:00 and 20:30 on one dry evening. The count may include repeat passes by the same bat. No other entrance or evening was observed.
```

### ultra: pass

```text
A volunteer counted 14 bats at the east entrance between 20:00 and 20:30 on one dry evening. Repeat passes by the same bat may be included. No other entrance or evening was observed.
```

### off: pass

```text
A volunteer counted 14 bats at the east entrance between 20:00 and 20:30 on one dry evening. The count may include repeat passes by the same bat. No other entrance or evening was observed.
```

## modes-en-077 · evidence

Source task:

> A note says “No corrosion was visible on the outside of the casing.” Rewrite for an inspection summary. The casing was not opened, and no chemical test was performed. Avoid extending the visual finding to the hidden interior.

### baseline: pass

```text
No corrosion was visible on the casing’s exterior. The casing was not opened, and no chemical testing was performed; the finding does not establish the condition of the interior.
```

### lite: pass

```text
No corrosion was visible on the outside of the casing. The casing was not opened, so the interior was not inspected. No chemical test was performed.
```

### full: pass

```text
No corrosion was visible on the casing’s exterior. The casing was not opened, so the interior was not inspected. No chemical test was performed.
```

### ultra: pass

```text
No corrosion was visible on the casing’s exterior. The casing was not opened, and no chemical test was performed; the interior was not assessed.
```

### off: pass

```text
No corrosion was visible on the outside of the casing. The casing was not opened, so its interior was not inspected. No chemical test was performed.
```

## modes-en-078 · evidence

Source task:

> Explain this survey result to a councillor: 64% of 150 people who voluntarily scanned a poster's QR code wanted more cycle parking. The poster was beside a cycle rack. The survey did not sample residents at random. Do not present it as 64% of all residents.

### baseline: pass

```text
Of the 150 people who voluntarily scanned the poster’s QR code, 64% wanted more cycle parking. The poster was beside a cycle rack, and respondents were not randomly sampled. The result describes these respondents, not all residents.
```

### lite: pass

```text
Of 150 people who voluntarily scanned the poster’s QR code, 64% wanted more cycle parking. The poster was beside a cycle rack, and residents were not sampled at random. The result describes these respondents, not all residents.
```

### full: pass

```text
Of 150 people who voluntarily scanned a poster’s QR code, 64% wanted more cycle parking. The poster was beside a cycle rack, and residents were not sampled at random. The result describes these respondents, not all residents.
```

### ultra: pass

```text
64% of 150 people who voluntarily scanned a poster’s QR code wanted more cycle parking. The poster was beside a cycle rack, and residents were not randomly sampled. The result describes these respondents, not all residents.
```

### off: pass

```text
Of 150 people who voluntarily scanned the poster’s QR code, 64% wanted more cycle parking. The poster was beside a cycle rack, which may have attracted people with an interest in cycling. Residents were not sampled at random, so this result describes the respondents—not all residents.
```

## modes-en-079 · evidence

Source task:

> Rewrite this supplied clinic scheduling note; give no medical advice: The 08:30 appointment was canceled because the clinician is unavailable. The note does not say why. Patients who had that appointment will be contacted to arrange another time. No replacement time has been set.

### baseline: pass

```text
The 08:30 appointment was canceled because the clinician is unavailable; no reason for the unavailability was given. Affected patients will be contacted to arrange another time. No replacement time has been set.
```

### lite: pass

```text
The 08:30 appointment was canceled because the clinician is unavailable. The note does not say why. Patients who had that appointment will be contacted to arrange another time. No replacement time has been set.
```

### full: pass

```text
The 08:30 appointment was canceled because the clinician is unavailable; the reason for that unavailability is not stated. Patients scheduled for that appointment will be contacted to arrange another time. No replacement time has been set.
```

### ultra: pass

```text
The 08:30 appointment was canceled because the clinician is unavailable; the reason for that unavailability is not stated. Patients booked for that appointment will be contacted to arrange another time. No replacement time has been set.
```

### off: pass

```text
The 08:30 appointment was canceled because the clinician is unavailable; the note does not state why. Patients who had that appointment will be contacted to arrange another time. No replacement time has been set.
```

## modes-en-080 · evidence

Source task:

> Write a concise quality note: A scale read 500 g for the check weight three times today. The check weight's certified mass is 500 g. Only that load was tested; the readings do not establish accuracy for lighter or heavier items. The check is not a full calibration.

### baseline: pass

```text
Today, the scale read 500 g on three checks using a certified 500 g weight. Only this load was tested; the results do not establish accuracy for lighter or heavier items. This check is not a full calibration.
```

### lite: pass

```text
The scale read 500 g three times today for a check weight with a certified mass of 500 g. Only that load was tested; the readings do not establish accuracy for lighter or heavier items. This check is not a full calibration.
```

### full: pass

```text
Today, the scale read 500 g three times for a check weight with a certified mass of 500 g. Only that load was tested; the readings do not establish accuracy for lighter or heavier items. This check is not a full calibration.
```

### ultra: pass

```text
Today, the scale read 500 g three times for a check weight with a certified mass of 500 g. Only this load was tested; the readings do not establish accuracy for lighter or heavier items. This was not a full calibration.
```

### off: pass

```text
Today, the scale read 500 g on three checks using a weight with a certified mass of 500 g. Only this load was tested; the readings do not establish accuracy for lighter or heavier items. This check is not a full calibration.
```

## modes-en-081 · translation

Source task:

> Translate the entire notice into English, keeping the placeholders unchanged: “Olá, {nome}. Seu cadastro foi recebido, mas ainda não foi aprovado. Você pode enviar o comprovante até 18h de 3 de fevereiro de 2029, no horário de Brasília. O envio é opcional nesta etapa; se houver exigência posterior, avisaremos por e-mail.”

### baseline: pass

```text
Hello, {nome}. Your registration has been received, but it has not yet been approved. You may submit the supporting document by 6 p.m. on February 3, 2029, Brasília time. Submission is optional at this stage; if it becomes required later, we will notify you by email.
```

### lite: pass

```text
Hello, {nome}. Your registration has been received, but it has not yet been approved. You may submit the supporting document by 6 p.m. on February 3, 2029, Brasília time. Submission is optional at this stage; if it becomes required later, we will notify you by email.
```

### full: pass

```text
Hello, {nome}. Your registration has been received but has not yet been approved. You may submit the supporting document by 6 p.m. on February 3, 2029, Brasília time. Submission is optional at this stage; if it becomes required later, we will notify you by email.
```

### ultra: pass

```text
Hello, {nome}. Your registration has been received but has not yet been approved. You may submit the supporting document by 6 p.m. on February 3, 2029, Brasília time. Submission is optional at this stage; if it becomes required later, we will notify you by email.
```

### off: pass

```text
Hello, {nome}. Your registration has been received, but it has not yet been approved. You may submit the supporting document by 6 p.m. on February 3, 2029, Brasília time. Submission is optional at this stage; if it becomes required later, we will notify you by email.
```

## modes-en-082 · translation

Source task:

> Translate into English without turning the estimate into a promise: “A oficina estima que o conserto leve de 4 a 6 dias úteis depois da chegada da peça. A peça ainda não foi despachada. Rui aprovou apenas o orçamento, não a troca do aparelho. Não sabemos quem retirou a tampa.”

### baseline: pass

```text
The repair shop estimates that the repair will take 4 to 6 business days after the part arrives. The part has not yet been shipped. Rui approved only the estimate, not the replacement of the device. We do not know who removed the cover.
```

### lite: pass

```text
The repair shop estimates that the repair will take 4 to 6 business days after the part arrives. The part has not yet been shipped. Rui approved only the quote, not replacement of the device. We do not know who removed the cover.
```

### full: pass

```text
The repair shop estimates that the repair will take 4 to 6 business days after the part arrives. The part has not yet been shipped. Rui approved only the cost estimate, not replacement of the device. We do not know who removed the cover.
```

### ultra: pass

```text
The repair shop estimates that the repair will take 4 to 6 business days after the part arrives. The part has not yet been shipped. Rui approved only the cost estimate, not replacement of the device. We do not know who removed the cover.
```

### off: pass

```text
The repair shop estimates that the repair will take 4 to 6 business days after the part arrives. The part has not yet been shipped. Rui approved only the cost estimate, not replacement of the device. We do not know who removed the cover.
```

## modes-en-083 · translation

Source task:

> Translate all of this into English and keep the deliberate humor: “Meu guarda-chuva pediu demissão na primeira rajada. Voltei para casa molhado, mas o caderno ficou seco dentro da mochila. Isso aconteceu na terça-feira; não sei se a loja vai aceitar a devolução.”

### baseline: pass

```text
My umbrella handed in its resignation at the first gust of wind. I got home wet, but the notebook stayed dry inside my backpack. This happened on Tuesday; I don't know whether the store will accept the return.
```

### lite: pass

```text
My umbrella resigned at the first gust. I went home soaked, but the notebook stayed dry inside my backpack. This happened on Tuesday; I don’t know whether the store will accept the return.
```

### full: pass

```text
My umbrella resigned at the first gust. I came home wet, but the notebook stayed dry inside my backpack. This happened on Tuesday; I don’t know whether the store will accept the return.
```

### ultra: pass

```text
My umbrella resigned at the first gust. I came home wet, but the notebook stayed dry inside my backpack. This happened on Tuesday; I don’t know whether the store will accept the return.
```

### off: pass

```text
My umbrella handed in its resignation at the first gust of wind. I came home soaked, but the notebook stayed dry inside my backpack. This happened on Tuesday; I don’t know whether the store will accept the return.
```

## modes-en-084 · translation

Source task:

> Translate this complete message into English: “La reserva no se confirma hasta que se recibe el pago. Puede pagar por transferencia o en la taquilla. Si el pago llega después del 14 de abril de 2029, se ofrecerá la siguiente fecha disponible; no se garantiza que sea esa misma semana.”

### baseline: pass

```text
The reservation is not confirmed until payment is received. You can pay by bank transfer or at the ticket office. If payment arrives after April 14, 2029, the next available date will be offered; there is no guarantee that it will be that same week.
```

### lite: pass

```text
The reservation is not confirmed until payment is received. You may pay by bank transfer or at the ticket office. If payment arrives after April 14, 2029, the next available date will be offered; there is no guarantee that it will be that same week.
```

### full: pass

```text
The reservation is not confirmed until payment is received. You may pay by bank transfer or at the ticket office. If payment arrives after April 14, 2029, the next available date will be offered; there is no guarantee it will be that same week.
```

### ultra: pass

```text
The reservation is not confirmed until payment is received. You may pay by bank transfer or at the ticket office. If payment arrives after April 14, 2029, the next available date will be offered; it is not guaranteed to be that same week.
```

### off: pass

```text
The reservation is not confirmed until payment is received. You may pay by bank transfer or at the ticket office. If payment arrives after April 14, 2029, the next available date will be offered; there is no guarantee that it will be in that same week.
```

## modes-en-085 · translation

Source task:

> Translate into English, preserving the command and path exactly: “Para comprobar la configuración, ejecute `visor check --local`. El comando no envía datos al servidor. El informe se guarda en /tmp/visor/revision.txt, salvo que el usuario indique otra carpeta.”

### baseline: pass

```text
To check the configuration, run `visor check --local`. The command does not send data to the server. The report is saved to /tmp/visor/revision.txt unless the user specifies another folder.
```

### lite: pass

```text
To check the configuration, run `visor check --local`. The command does not send data to the server. The report is saved to /tmp/visor/revision.txt unless the user specifies another folder.
```

### full: pass

```text
To check the configuration, run `visor check --local`. The command does not send data to the server. The report is saved to /tmp/visor/revision.txt unless the user specifies another folder.
```

### ultra: pass

```text
To check the configuration, run `visor check --local`. The command does not send data to the server. The report is saved to /tmp/visor/revision.txt unless the user specifies another folder.
```

### off: pass

```text
To check the configuration, run `visor check --local`. The command does not send data to the server. The report is saved to /tmp/visor/revision.txt unless the user specifies another folder.
```

## modes-en-086 · translation

Source task:

> Translate the whole paragraph into English: “Respondieron 32 de las 80 personas invitadas por correo. No se eligió una muestra aleatoria: la invitación se envió a quienes habían participado el año anterior. El 75 % de quienes respondieron pidió repetir el taller; eso no representa al conjunto del barrio.”

### baseline: pass

```text
32 of the 80 people invited by email responded. No random sample was selected: the invitation was sent to those who had participated the previous year. 75% of respondents asked for the workshop to be held again; this does not represent the neighborhood as a whole.
```

### lite: pass

```text
Of the 80 people invited by email, 32 responded. No random sample was selected: the invitation was sent to those who had participated the previous year. Of those who responded, 75% asked for the workshop to be held again; this does not represent the neighborhood as a whole.
```

### full: pass

```text
Of the 80 people invited by email, 32 responded. The sample was not randomly selected: invitations were sent to people who had participated the previous year. Of those who responded, 75% asked for the workshop to be repeated; that does not represent the neighborhood as a whole.
```

### ultra: pass

```text
Of the 80 people invited by email, 32 responded. The sample was not random: invitations were sent to people who had participated the previous year. Of those who responded, 75% asked to repeat the workshop; this does not represent the neighborhood as a whole.
```

### off: pass

```text
Of the 80 people invited by email, 32 responded. A random sample was not selected: the invitation was sent to those who had participated the previous year. Of those who responded, 75% asked for the workshop to be held again; that does not represent the neighborhood as a whole.
```

## modes-en-087 · translation

Source task:

> Translate this into English without adding policy advice: “Vous devez rendre le badge avant de quitter le bâtiment. Vous pouvez conserver la pochette. Si l'accueil est fermé, déposez le badge dans la boîte marquée RETOUR-3. Cette exception ne vous autorise pas à emporter le badge chez vous.”

### baseline: pass

```text
You must return the badge before leaving the building. You may keep the pouch. If reception is closed, place the badge in the box marked RETOUR-3. This exception does not authorize you to take the badge home.
```

### lite: pass

```text
You must return the badge before leaving the building. You may keep the pouch. If reception is closed, place the badge in the box marked RETOUR-3. This exception does not authorize you to take the badge home.
```

### full: pass

```text
You must return the badge before leaving the building. You may keep the pouch. If reception is closed, place the badge in the box marked RETOUR-3. This exception does not allow you to take the badge home.
```

### ultra: pass

```text
You must return the badge before leaving the building. You may keep the sleeve. If reception is closed, place the badge in the box marked RETOUR-3. This exception does not allow you to take the badge home.
```

### off: pass

```text
You must return the badge before leaving the building. You may keep the pouch. If reception is closed, place the badge in the box marked RETOUR-3. This exception does not authorize you to take the badge home.
```

## modes-en-088 · translation

Source task:

> Translate all content into English: “Le débit mesuré est passé de 12 à 15 litres par minute, soit une hausse de 25 %. Les mesures ont été prises sur le même tuyau, mais à deux températures différentes. Nous n'avons pas établi que le nouveau robinet a causé cette hausse.”

### baseline: pass

```text
The measured flow rate increased from 12 to 15 liters per minute, a rise of 25%. The measurements were taken on the same pipe, but at two different temperatures. We have not established that the new faucet caused this increase.
```

### lite: pass

```text
The measured flow rate increased from 12 to 15 liters per minute, a 25% increase. The measurements were taken on the same pipe, but at two different temperatures. We have not established that the new faucet caused this increase.
```

### full: pass

```text
The measured flow rate increased from 12 to 15 liters per minute, a 25% increase. The measurements were taken on the same pipe, but at two different temperatures. We have not established that the new faucet caused this increase.
```

### ultra: pass

```text
The measured flow rate rose from 12 to 15 liters per minute, a 25% increase. Measurements were taken on the same pipe but at two different temperatures. We have not established that the new faucet caused this increase.
```

### off: pass

```text
The measured flow rate increased from 12 to 15 liters per minute, a 25% increase. The measurements were taken on the same pipe, but at two different temperatures. We have not established that the new faucet caused this increase.
```

## modes-en-089 · translation

Source task:

> Translate into English while retaining a courteous, uncertain tone: “Merci, Camille, pour votre signalement. La fenêtre a été refermée après votre appel, mais le registre ne précise pas par qui. Nous avons demandé une vérification du verrou; aucun résultat n'est encore disponible.”

### baseline: pass

```text
Thank you, Camille, for bringing this to our attention. The window was closed again after your call, but the log does not specify by whom. We have requested a check of the lock; no results are available yet.
```

### lite: pass

```text
Thank you, Camille, for reporting this. The window was closed again after your call, but the log does not specify by whom. We have requested a check of the lock; no results are available yet.
```

### full: pass

```text
Thank you, Camille, for reporting this. The window was closed again after your call, but the log does not specify by whom. We have requested a check of the lock; no results are available yet.
```

### ultra: pass

```text
Thank you, Camille, for reporting this. The window was closed again after your call, but the log does not specify by whom. We requested a check of the lock; no results are available yet.
```

### off: pass

```text
Thank you, Camille, for your report. The window was closed again after your call, but the log does not specify by whom. We have requested a check of the lock; no results are available yet.
```

## modes-en-090 · translation

Source task:

> Translate into English: “Die Lieferung umfasst acht Kisten, nicht acht einzelne Geräte. Jede Kiste enthält drei Geräte. Zwei Kisten bleiben bis zur Prüfung gesperrt. Die Prüfung ist geplant, aber noch nicht durchgeführt.”

### baseline: pass

```text
The delivery consists of eight crates, not eight individual devices. Each crate contains three devices. Two crates remain on hold pending inspection. The inspection is planned but has not yet been carried out.
```

### lite: pass

```text
The delivery consists of eight crates, not eight individual devices. Each crate contains three devices. Two crates remain on hold until the inspection. The inspection is planned but has not yet been carried out.
```

### full: pass

```text
The delivery contains eight crates, not eight individual devices. Each crate contains three devices. Two crates remain on hold until the inspection. The inspection is planned but has not yet been carried out.
```

### ultra: pass

```text
The delivery contains eight crates, not eight individual devices. Each crate contains three devices. Two crates remain on hold until the inspection. The inspection is planned but has not yet been carried out.
```

### off: pass

```text
The delivery consists of eight crates, not eight individual devices. Each crate contains three devices. Two crates remain on hold until the inspection. The inspection is planned but has not yet been carried out.
```

## modes-en-091 · translation

Source task:

> Translate the entire policy into English: “Eine Teilnahme ohne Anmeldung ist nur möglich, wenn Plätze frei sind. Auch dann müssen Minderjährige eine schriftliche Zustimmung mitbringen. Für Erwachsene ist diese Zustimmung nicht erforderlich. Die Anmeldung garantiert keinen Parkplatz.”

### baseline: pass

```text
Participation without registration is only possible if spaces are available. Even then, minors must bring written consent. Adults do not need this consent. Registration does not guarantee a parking space.
```

### lite: pass

```text
Participation without registration is possible only if spaces are available. Even then, minors must bring written consent. Adults do not need this consent. Registration does not guarantee a parking space.
```

### full: pass

```text
Participation without registration is possible only if spaces are available. Even then, minors must bring written consent. Adults do not need this consent. Registration does not guarantee a parking space.
```

### ultra: pass

```text
Participation without registration is possible only if spaces are available. Even then, minors must bring written consent. Adults do not need this consent. Registration does not guarantee a parking space.
```

### off: pass

```text
Participation without registration is possible only if places are available. Even then, minors must bring written consent. Adults do not need this consent. Registration does not guarantee a parking space.
```

## modes-en-092 · translation

Source task:

> Translate into English and keep the quotation mark distinction: “Im Protokoll steht wörtlich: „Noch nicht freigegeben.“ Das bedeutet nicht, dass der Antrag abgelehnt wurde. Die Prüfung läuft weiter; ein Termin für die Entscheidung wurde nicht genannt.”

### baseline: pass

```text
“The minutes state verbatim: ‘Not yet approved.’ This does not mean that the application was rejected. The review is ongoing; no date for the decision was given.”
```

### lite: pass

```text
The minutes state verbatim (translated): “Not yet approved.” This does not mean that the application was rejected. The review is ongoing; no date for the decision was given.
```

### full: pass

```text
The minutes state verbatim (translated): “Not yet approved.” This does not mean that the application was rejected. The review is ongoing; no date was given for the decision.
```

### ultra: pass

```text
The minutes state verbatim: “Not yet approved.” This does not mean the application was rejected. The review continues; no date was given for the decision.
```

### off: pass

```text
The minutes state verbatim: “Not yet approved.” This does not mean that the application was rejected. The review is continuing; no date was given for the decision.
```

## modes-en-093 · translation

Source task:

> Translate the entire Japanese notice into English: 「予約の変更は無料ですが、前日の正午までに連絡が必要です。当日の変更は受け付けません。キャンセルの場合、返金できるかどうかは支払い方法によって異なります。返金が必ずあるとは書かれていません。」

### baseline: pass

```text
Changes to reservations are free, but you must contact us by noon on the previous day. Same-day changes are not accepted. In the event of cancellation, whether a refund is possible depends on the payment method. The notice does not state that a refund is guaranteed.
```

### lite: pass

```text
Reservation changes are free, but you must contact us by noon on the day before the reservation. Same-day changes are not accepted. If you cancel, whether a refund is possible depends on the payment method. The notice does not state that a refund is guaranteed.
```

### full: pass

```text
Reservation changes are free, but you must contact us by noon the day before. Same-day changes are not accepted. If you cancel, whether a refund is possible depends on the payment method. The notice does not state that a refund is guaranteed.
```

### ultra: pass

```text
Reservation changes are free, but you must contact us by noon the day before. Same-day changes are not accepted. For cancellations, refund eligibility depends on the payment method. The notice does not state that a refund is guaranteed.
```

### off: pass

```text
Changes to reservations are free of charge, but you must contact us by noon on the day before. Same-day changes are not accepted. In the event of cancellation, whether a refund is possible depends on the payment method. The notice does not state that a refund is guaranteed.
```

## modes-en-094 · translation

Source task:

> Translate into English, retaining the identifiers exactly: 「センサー S-06 の温度は 22.4 °C でした。これは午前9時の1回の測定です。午後の温度は測定していません。保存先は /data/S-06.csv です。測定した人の名前は記録されていません。」

### baseline: pass

```text
The temperature recorded by sensor S-06 was 22.4 °C. This was a single measurement taken at 9 a.m. The afternoon temperature was not measured. The save location is /data/S-06.csv. The name of the person who took the measurement was not recorded.
```

### lite: pass

```text
The temperature recorded by sensor S-06 was 22.4 °C. This was a single measurement at 9 a.m. The afternoon temperature was not measured. The save location is /data/S-06.csv. The name of the person who took the measurement was not recorded.
```

### full: pass

```text
The temperature at sensor S-06 was 22.4 °C. This was a single measurement taken at 9 a.m. The afternoon temperature was not measured. The storage location is /data/S-06.csv. The name of the person who took the measurement was not recorded.
```

### ultra: pass

```text
Sensor S-06 recorded a temperature of 22.4 °C. This was a single measurement at 9 a.m. The afternoon temperature was not measured. The save location is /data/S-06.csv. The name of the person who took the measurement was not recorded.
```

### off: pass

```text
The temperature of sensor S-06 was 22.4 °C. This was a single measurement taken at 9 a.m. The afternoon temperature was not measured. The save location is /data/S-06.csv. The name of the person who took the measurement was not recorded.
```

## modes-en-095 · translation

Source task:

> Translate the whole notice into English: “只有在经理批准并且付款到账后，订单才能发货。发送付款截图不等于付款到账。您可以选择自提，但仍需满足这两个条件。通知没有给出发货日期。”

### baseline: pass

```text
The order can be shipped only after the manager has approved it and payment has been received. Sending a screenshot of the payment is not the same as payment being received. You may choose to pick up the order yourself, but both conditions must still be met. The notice does not give a shipping date.
```

### lite: pass

```text
The order can be shipped only after the manager has approved it and payment has been received. Sending a payment screenshot does not mean that payment has been received. You may choose to pick up the order, but both conditions must still be met. The notice does not give a shipping date.
```

### full: pass

```text
The order can be shipped only after the manager has approved it and payment has been received. Sending a payment screenshot does not mean that payment has been received. You may choose pickup, but both conditions must still be met. The notice does not give a shipping date.
```

### ultra: pass

```text
The order can be shipped only after the manager approves it and payment has been received. Sending a payment screenshot does not mean payment has been received. You may choose pickup, but both conditions still apply. The notice gives no shipping date.
```

### off: pass

```text
The order can be shipped only after the manager has approved it and payment has been received. Sending a screenshot of the payment does not mean that payment has been received. You may choose to pick up the order yourself, but both conditions must still be met. The notice does not give a shipping date.
```

## modes-en-096 · translation

Source task:

> Translate into English, preserving quoted code and uncertainty: “日志显示 ‘ERR_42’，但这不能证明文件已损坏。检查程序还没有读取完整文件。工程师认为网络中断可能是原因之一，目前没有确定原因。”

### baseline: pass

```text
The log shows ‘ERR_42’, but this does not prove that the file is corrupted. The checking program has not yet read the entire file. Engineers believe a network interruption may be one possible cause; the cause has not yet been determined.
```

### lite: pass

```text
The logs show ‘ERR_42’, but this does not prove that the file is corrupted. The checking program has not yet read the entire file. Engineers believe a network interruption may be one possible cause; the cause has not yet been determined.
```

### full: pass

```text
The log shows ‘ERR_42’, but this does not prove that the file is corrupted. The checking program has not yet read the entire file. Engineers believe a network interruption may be one possible cause. No cause has been confirmed.
```

### ultra: pass

```text
The logs show ‘ERR_42’, but this does not prove the file is corrupted. The checking program has not yet read the entire file. Engineers think a network interruption may be one possible cause; the cause remains undetermined.
```

### off: pass

```text
The logs show ‘ERR_42’, but this does not prove that the file is corrupted. The checking program has not yet read the entire file. The engineers believe that a network interruption may be one possible cause; no cause has been established yet.
```

## modes-en-097 · translation

Source task:

> Translate the complete message into English: “Il pacco è stato lasciato alla reception dopo la telefonata di Daria. Non sappiamo chi lo abbia consegnato. La reception ha registrato l'arrivo alle 11:45. Questo orario non indica quando il pacco è partito dal magazzino.”

### baseline: pass

```text
The package was left at reception after Daria's phone call. We do not know who delivered it. Reception recorded its arrival at 11:45. This time does not indicate when the package left the warehouse.
```

### lite: pass

```text
The package was left at reception after Daria's phone call. We do not know who delivered it. Reception recorded its arrival at 11:45. This time does not indicate when the package left the warehouse.
```

### full: pass

```text
The package was left at reception after Daria’s phone call. We do not know who delivered it. Reception recorded its arrival at 11:45. This time does not indicate when the package left the warehouse.
```

### ultra: pass

```text
The package was left at reception after Daria’s phone call. We do not know who delivered it. Reception recorded its arrival at 11:45. This time does not indicate when the package left the warehouse.
```

### off: pass

```text
The package was left at reception after Daria's phone call. We do not know who delivered it. Reception recorded its arrival at 11:45. This time does not indicate when the package left the warehouse.
```

## modes-en-098 · translation

Source task:

> Translate into English without changing the currency or estimate: “Il preventivo è di 1.250 euro, IVA inclusa. Il montaggio, stimato in 180–240 euro, è facoltativo e non è compreso. Il prezzo del prodotto è valido fino al 9 ottobre 2029; non è una scadenza obbligatoria per l'acquisto.”

### baseline: pass

```text
The quote is 1,250 euros, including VAT. Installation, estimated at 180–240 euros, is optional and is not included. The product price is valid until October 9, 2029; this is not a mandatory deadline for purchasing.
```

### lite: pass

```text
The quote is 1,250 euros, including VAT. Installation, estimated at 180–240 euros, is optional and is not included. The product price is valid until October 9, 2029; this is not a mandatory deadline for purchasing.
```

### full: pass

```text
The quote is 1,250 euros, including VAT. Installation, estimated at 180–240 euros, is optional and not included. The product price is valid until October 9, 2029; this is not a mandatory purchase deadline.
```

### ultra: pass

```text
The quote is 1,250 euros, including VAT. Installation, estimated at 180–240 euros, is optional and not included. The product price is valid until 9 October 2029; this is not a mandatory purchase deadline.
```

### off: pass

```text
The quote is 1,250 euros, including VAT. Assembly, estimated at 180–240 euros, is optional and is not included. The product price is valid until October 9, 2029; this is not a mandatory deadline for purchasing.
```

## modes-en-099 · translation

Source task:

> Translate the entire Russian notice into English: «Архив открыт по средам с 10:00 до 14:00. Посетители могут фотографировать разрешённые документы, но должны зарегистрировать каждый запрошенный ящик. Фотосъёмка не обязательна. Закрытые фонды доступны только после письменного разрешения.»

### baseline: pass

```text
The archive is open on Wednesdays from 10:00 to 14:00. Visitors may photograph documents for which photography is permitted, but must register each box requested. Photography is not mandatory. Restricted collections are accessible only after written permission has been granted.
```

### lite: pass

```text
The archive is open on Wednesdays from 10:00 to 14:00. Visitors may photograph permitted documents, but must register each box requested. Photography is not mandatory. Restricted collections are accessible only after written permission has been granted.
```

### full: pass

```text
The archive is open on Wednesdays from 10:00 to 14:00. Visitors may photograph permitted documents but must register each box requested. Photography is not mandatory. Restricted collections are accessible only after written permission has been granted.
```

### ultra: pass

```text
The archive is open on Wednesdays from 10:00 to 14:00. Visitors may photograph permitted documents but must register each box requested. Photography is optional. Restricted collections are accessible only after written permission has been granted.
```

### off: pass

```text
The archive is open on Wednesdays from 10:00 to 14:00. Visitors may photograph documents for which photography is permitted, but must register each box requested. Photography is not mandatory. Restricted collections are accessible only after written permission has been granted.
```

## modes-en-100 · translation

Source task:

> Translate into English and preserve the sample caveat: «В опросе участвовали 90 добровольцев из одного клуба. Из них 54 поддержали вечерние занятия. Участников не выбирали случайным образом. Эти данные не показывают мнение всех жителей города.»

### baseline: pass

```text
The survey involved 90 volunteers from one club. Of these, 54 supported evening classes. Participants were not selected randomly. These data do not represent the views of all city residents.
```

### lite: pass

```text
The survey included 90 volunteers from one club. Of these, 54 supported evening classes. Participants were not selected randomly. These data do not show the views of all city residents.
```

### full: pass

```text
The survey included 90 volunteers from one club. Of these, 54 supported evening classes. Participants were not randomly selected. These data do not show the views of all city residents.
```

### ultra: pass

```text
The survey included 90 volunteers from one club. Of these, 54 supported evening classes. Participants were not randomly selected. These data do not represent the views of all city residents.
```

### off: pass

```text
The survey involved 90 volunteers from one club. Of these, 54 supported evening classes. Participants were not selected randomly. These data do not show the opinions of all city residents.
```

