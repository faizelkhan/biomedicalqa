import argparse


def get_train_test_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--num-epochs", type=int, default=5)
    parser.add_argument("--num-epochs-pretrain", type=int, default=5)
    parser.add_argument("--lr", type=float, default=3e-5)
    parser.add_argument("--num_experts", type=int, default=4)
    parser.add_argument("--num-visuals", type=int, default=10)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--save-dir", type=str, default="save/")
    parser.add_argument("--pretrain", action="store_true")
    parser.add_argument("--train", action="store_true")
    parser.add_argument("--eval", action="store_true")
    parser.add_argument("--run-name", type=str, default="multitask_distilbert")
    parser.add_argument("--model-type", type=str, default="distilbert")
    parser.add_argument("--loss-type", type=str, default="focalloss")
    parser.add_argument(
        "--use_cache", action="store_true"
    )  # only use_cache if the argument is present
    parser.add_argument("--do-train", action="store_true")
    parser.add_argument("--do-eval", action="store_true")
    parser.add_argument("--sub-file", type=str, default="")
    parser.add_argument("--visualize-predictions", action="store_true")
    parser.add_argument("--eval-every", type=int, default=100)
    parser.add_argument("--dim", type=int, default=768)
    parser.add_argument("--hidden_dim", type=int, default=768 * 4)
    parser.add_argument(
        "--num_aug_pretrain",
        default=4,
        required=False,
        type=int,
        help="number of augmented sentences per original sentence for pretraining",
    )
    parser.add_argument(
        "--num_aug",
        default=4,
        required=False,
        type=int,
        help="number of augmented sentences per original sentence",
    )

    args = parser.parse_args()
    return args


DATASET_CONFIG = {
    "train": [
        #"datasets/indomain_train/squad",
        "datasets/oodomain_train/bioasq",
    ],
    "finetune": [
        "datasets/oodomain_train/bioasq",
    ],
    "ood_val": [
        "datasets/oodomain_val/bioasq",
    ],
    "test": [
        "datasets/oodomain_test/bioasq",
    ],
}
