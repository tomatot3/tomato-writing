# Worked examples

These are synthetic editing exercises, not claims about real studies. Use the decision pattern, not the specific wording or field assumptions.

## 1. A proposed task mistaken for a gap

**Draft:** 'Existing environmental studies do not use our graph architecture. A graph architecture is therefore needed for reliable estimation.'

**Available evidence:** Two cited studies estimate each sensor independently. During documented flooding events, neighbouring sensors share failures and missingness.

**Revision direction:** Establish the observed dependence and its consequence for the independent-sensor assumption. Then introduce joint modelling as the authors' approach. Do not assert that graphs are the only possible solution or that all environmental studies ignore dependence.

**Possible passage:** 'Flooding can interrupt several neighbouring sensors at once, producing gaps that are spatially related. The two sensor-wise estimators treat missing observations independently. We examine whether modelling dependence between neighbouring sensors improves estimates during these shared interruptions.'

The problem survives without the proposed architecture's name. An evaluation is still needed to establish improvement.

## 2. Compression that removes the mechanism

**Draft:** 'The method uses spatial hierarchy, parameterization, and topological compatibility.'

**Available mechanism:** Divide a domain into subregions; place one component in each; vary its curvature and size; allow adjoining components only when their boundary ports match.

**Possible revision:** 'The method divides the domain into subregions and places a component in each. Curvature and size control local shape, while matching ports determine which neighbouring components can connect.'

This is longer and easier to understand. If these are essential distinctions in a cited method, do not compress them away merely to shorten related work.

## 3. An observational result and an imagined objection

**Draft:** 'Treatment use was associated with fewer admissions. However, the finding may not apply to genetically distinct populations, alternative health systems, or future climates.'

**Available evidence:** A clinic-based observational cohort; adjusted rate ratio 0.82 with 95% CI 0.73–0.93. No analysis of genetic groups or climate.

**Possible revision:** 'In the clinic cohort, treatment use was associated with a lower admission rate after adjustment for the measured covariates (rate ratio 0.82, 95% CI 0.73–0.93).'

Keep the association and meaningful uncertainty. Remove speculative objections. Do not rewrite as a causal treatment effect or hide design-related limitations where they matter to interpretation.

## 4. A theoretical condition that must survive simplification

**Draft:** 'The algorithm always returns the optimum. Under time pressure, it returns the best solution available.'

**Available mechanism:** A valid branch-and-bound bound; finite candidates; complete termination establishes optimality; a time limit can interrupt search.

**Possible revision:** 'When the search finishes without reaching the time limit, the returned solution is optimal within the finite candidate set. An interrupted search returns the best feasible solution found.'

The condition is part of the theorem's application, not defensive decoration. If the implementation can return no feasible solution, preserve that fact where the return behavior is defined.

## 5. Humanities evidence without a technological deficit

**Draft:** 'The archive needs a digital classification framework, which existing scholarship lacks.'

**Available evidence:** Letters and later memoirs give different dates for the same journey. Prior accounts rely mainly on memoir chronology. The present study compares dated letters, postmarks, and travel records.

**Revision direction:** State the chronological conflict and what resolving it changes in the historical account. Explain the comparison of evidence. Do not invent a need for machine learning, a benchmark, or a universal digital classification.

A contribution can be a better-supported interpretation and a transparent account of uncertainty. It need not promise a new automated system.

## 6. A numerical range with the wrong implied meaning

**Draft:** 'Agreement was 81–96%, demonstrating robust performance.'

**Available evidence:** Six parameter settings yield agreement values in that range; no interval estimation was performed.

**Possible revision:** 'Across the six parameter settings, agreement ranged from 81% to 96%.'

Add an explanation of the settings or the relevant pattern if it serves the result. Do not label the range a confidence interval or infer robustness from the range alone.

## 7. Translating operation order

**Chinese source:** '先将图像区域分组，经人工校正后矢量化，支持整组移动和单个元素删除。'

**Misleading English:** 'The system automatically recovers editable objects after vectorization.'

**Possible revision:** 'Image regions are grouped, manually corrected, and then vectorized. The resulting objects support group movement and deletion of individual elements.'

Preserve sequence, manual intervention, and both operation levels. 'Automatically' and 'recovers' add claims absent from the source.

## 8. Results and Discussion with different functions

**Result:** 'The joint method selected shorter routes near congested junctions and reduced median travel time by 6 minutes.'

**Weak Discussion:** Repeats the junction-by-junction selections and the whole table.

**Discussion direction:** Explain what the result suggests about interactions between local route choices and network congestion, using the actual controls and evidence. Do not infer a causal mechanism if the comparison does not isolate it. Identify what would change when demand patterns or constraints change, if that boundary matters.

## 9. A sentence that should remain

**Sentence:** 'Samples were dried at 60 °C for 24 h before weighing.'

The object, action, conditions, and order are clear. Replacing it with 'We implemented a controlled drying procedure...' adds abstraction. Retain the original unless another context-specific issue is identified.

## 10. Terminology that should not be globally unified

A paper distinguishes a physical specimen, its scan, a fitted model, and a rendered view. Calling all four 'the digital object' obscures where measurements, fitting errors, and visual changes occur.

Use stable names for each referent. When a later paragraph concerns only the rendering, a short local term is fine. Terminology consistency is conceptual, not just lexical.

## 11. A repeated condition with different possible jobs

**Draft pattern:** An abstract introduces a model fitted under fixed illumination. The Methods opening, fitting subsection, Results opening and Discussion each repeat that illumination is fixed and the model is fitted to the observed images.

**Decision:** Keep the concise abstract scope and the formal Methods specification. If a Results comparison uses the same illumination for both methods, retain the compact comparison condition. Delete a Results preamble that simply reteaches fitting. In Discussion, explain what fixed illumination means for interpreting material estimates if that consequence is relevant; do not repeat the fitting sequence or speculate about untested lighting failures.

The repeated words are not the problem. The issue is whether each occurrence adds a new role or just makes the reader restart. Do not remove caption conditions that are needed to interpret a figure independently.
