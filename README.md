# KGRED

This is an evaluation script.

### Data Format

The result data should be a csv file including four columns.

For details, refer to [this file](https://github.com/Caesar-s1mple/KGRED-eval/blob/main/data/recon/recon_wiki80_result.csv).

### Evaluation

```bash
python eval.py --test-file <result_data> --NA <NA_name>
```

`result_data` is the csv file illustrated in [Data Format](# "Data Format").

`NA_name` is the name of NA tag in your result data. If no NA is contained in your dataset, do not set this.

