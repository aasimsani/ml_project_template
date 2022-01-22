from argparse import ArgumentParser
import pytorch_lightning as pl
from training.train import train
from deployment.deploy import app
import uvicorn


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--train",
                        help="Train model",
                        action="store_true"
                        )

    parser.add_argument("--deploy",
                        help="Deploy model",
                        action="store_true"
                        )
    parser = pl.Trainer.add_argparse_args(parser)
    args = parser.parse_args()

    if args.train:
        train(args)

    if args.deploy:
        uvicorn.run(app)