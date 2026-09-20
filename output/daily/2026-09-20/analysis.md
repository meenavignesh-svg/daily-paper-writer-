## Scope of the evidence

The supplied bibliography contains only a small number of papers directly concerned with protein-function prediction. The clearest direct study is Gligorijević et al., *Structure-based protein function prediction using graph convolutional networks* (2021). Bordin et al.’s review of machine learning and protein knowledge, Yu et al.’s review of metalloproteins, and the papers on protein language models, interaction prediction, and sequence-based screening provide relevant context. Several other records concern clinical prediction, cancer biology, drug response, virtual screening, or protein structure prediction and should not be treated as direct evidence about protein-function annotation.

The metadata supplied do not establish the datasets, train/test splits, numerical results, or evaluation metrics for most of the relevant studies. Specific claims about those details therefore require full-text checking [VERIFY].

## How machine learning is being used

### Sequence-based representation learning

A major direction is the use of protein language models and transformer-derived embeddings. These models are trained on large collections of protein sequences and can provide numerical representations for downstream tasks such as functional classification, activity prediction, ligand or substrate specificity, and variant prioritization. Bordin et al. discuss this broader transition toward learned protein representations, while Tran et al. describe the use of protein language models in directed evolution.

The latter should be interpreted cautiously: its title indicates sequence optimization guided by language models and epistatic interactions, not necessarily conventional function annotation such as Gene Ontology or Enzyme Commission prediction. Whether the study predicts biochemical function directly, or instead ranks variants for experimental testing, must be verified from the full text [VERIFY].

Transformers are also being applied to sequence-based virtual screening. This may overlap with function prediction when the target is ligand binding or biochemical activity, but virtual screening and protein-function annotation are distinct tasks. The endpoint, labels, and evaluation design in Zhang et al. require verification [VERIFY].

### Structure-based models

Gligorijević et al. provide the strongest direct example of structure-based function prediction. Their use of graph convolutional networks indicates that proteins are represented as graphs, allowing a model to learn from structural relationships rather than sequence order alone. Such models can, in principle, capture spatially neighboring residues, structural motifs, and relationships between residues that are distant in sequence but close in three-dimensional space.

The supplied record does not show whether the graphs represent residues, atoms, or another structural unit, nor which structural features were used [VERIFY]. It also does not establish whether the structures were experimentally determined, computationally predicted, or drawn from a mixture of sources [VERIFY].

AlphaFold and AlphaFold 3 are important enabling technologies because predicted structures and biomolecular complexes can supply structural information for downstream analyses. However, structure prediction is not itself protein-function prediction. A highly accurate structural model does not guarantee correct assignment of biochemical activity, biological process, cellular localization, or molecular interaction specificity.

### Specialized functional prediction

The review by Yu et al. focuses on metalloproteins, where machine learning may be applied to metal-binding-protein classification, metal-binding-site detection, coordination geometry, or metal-dependent enzyme function. These tasks illustrate that “protein function” is not a single prediction problem: the label may describe an entire protein, a catalytic site, a binding residue, a ligand preference, or a broader ontology term.

The supplied evidence does not identify the metalloprotein databases, negative examples, or benchmark protocols used in that review [VERIFY].

### Network and interaction-informed prediction

Graph-learning methods are also being applied to protein–protein interaction prediction, as in Gao et al. Interaction networks can provide functional evidence, since proteins with related interaction partners may participate in related pathways. Nevertheless, interaction prediction is an intermediate or related task, not equivalent to predicting protein function. The same distinction applies to protein–protein docking: learned docking or scoring models may help characterize molecular interactions, but they do not automatically provide functional annotations.

## Datasets and labels

The relevant studies may draw on several broad categories of data:

- protein sequence databases used to train language models;
- experimentally curated functional annotations;
- Gene Ontology or Enzyme Commission labels;
- protein structures and predicted structures;
- protein–protein interaction networks;
- specialized collections of metalloproteins or metal-binding sites;
- experimentally measured activity, binding, or variant-fitness data.

These categories are evident from the topics represented in the bibliography, but the supplied records do not specify which particular databases were used in the direct prediction studies. The evidence therefore cannot support definitive claims about UniProt, Gene Ontology, PDB, AlphaFold DB, CAFA benchmarks, enzyme databases, or metalloprotein-specific resources without full-text verification [VERIFY].

A central methodological issue is how the data are divided. Random sequence-level splits can place very similar proteins in both training and test sets, producing apparently strong performance through homology rather than genuine generalization. More demanding evaluations use sequence-identity or homology-aware splits, family-level splits, or temporal splits. Whether the cited studies use such safeguards is not apparent from the bibliography [VERIFY].

## Evaluation metrics

The supplied evidence does not report the metrics used by the relevant papers. For multilabel protein-function prediction, commonly considered measures include precision, recall, and F1 score; area under the receiver-operating-characteristic curve and area under the precision–recall curve; and ranking-based measures such as precision at a specified cutoff. Ontology-aware evaluation may also use semantic similarity or metrics such as S-min in Gene Ontology benchmarks [VERIFY].

Different prediction targets require different measures. Protein-level classification may use macro- or micro-averaged F1, whereas residue-level binding-site prediction may use sensitivity, specificity, Matthews correlation coefficient, or site-level precision and recall [VERIFY]. Enzyme-function prediction may be reported using accuracy or hierarchical classification measures, but accuracy can be misleading when classes are imbalanced [VERIFY]. Structural or interaction-prediction papers may instead use measures of contact recovery, docking quality, or interaction ranking, which should not be conflated with functional-annotation metrics.

Reported performance should therefore be interpreted together with class balance, annotation frequency, confidence thresholds, and the choice of split—not as a single universal score.

## Remaining limitations

Several limitations recur across this area:

1. **Incomplete and noisy labels.** Functional databases contain uncertain, incomplete, and unevenly distributed annotations. Absence of an annotation does not necessarily mean absence of the function, making negative-example construction difficult [VERIFY].

2. **Homology leakage.** Closely related sequences across training and test sets can inflate performance. This is especially problematic for models evaluated on random rather than homology-aware splits.

3. **Long-tailed functions and class imbalance.** Common functions have many examples, while rare activities and poorly studied protein families have few or no reliable labels. Aggregate metrics can therefore obscure poor performance on biologically important rare classes.

4. **Limited out-of-distribution generalization.** Models may perform well on proteins resembling their training data but fail on remote homologues, novel folds, unusual domains, disordered proteins, or proteins from underrepresented organisms [VERIFY].

5. **Structure and context are incomplete.** A static structure may not capture conformational dynamics, post-translational modifications, cellular localization, cofactors, environmental conditions, or macromolecular context. Predicted structures add further uncertainty, even when geometric confidence is high.

6. **Correlation is not mechanism.** Sequence or structure features associated with a function may support prediction without explaining the causal biochemical mechanism. Interpretability methods can identify influential residues or regions, but such explanations still require experimental validation [VERIFY].

7. **Limited experimental validation.** Computational predictions are often evaluated against existing annotations rather than prospective laboratory measurements. The extent of prospective validation in the cited studies is not clear from the supplied records [VERIFY].

Overall, machine learning is expanding protein-function prediction from manually engineered sequence features toward learned sequence representations, structural graphs, and multimodal biological information. The principal unresolved issue is not simply model architecture but trustworthy evaluation: reliable labels, leakage-resistant splits, appropriate metrics, calibrated uncertainty, and experimental confirmation of predictions on genuinely novel proteins.