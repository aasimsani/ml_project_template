import torch
import numpy as np
import pytorch_lightning as pl
from pytorch_lightning.loggers import WandbLogger

# NOTE: Make sure you've initalized and setup weights and biases
# before you do this
wandb_logger = WandbLogger()

# Importing the model
# from models.litmodels import YOURMODEL

# Import PyTorch Datasets
# from data.datasets import YOURDATASET

def worker_init_fn(worker_id):
    """Initalize a worker with an actual random seed
     on each thread - This is a required due to a bug in PyTorch
    :param worker_id: Worker ID which is passed by the data loader
    :type worker_id: int
    """
    np.random.seed(np.random.get_state()[1][0] + worker_id)


def collate_fn(batch):
    """This function collates a batch together to pass out from
     a data loader.
    :param batch: A batch from the dataloader
    :type batch: list
    :return: A tuple of the batch with targets and images zipped together
    :rtype: tuple
    """
    return tuple(zip(*batch))

def train(args):

    # Load data

    # dataset = YOURDATASET(args)
    # dataloader = torch.utls.data.DataLoader(dataset,
    # 										batch_size=args.batch_size,
    # 										shuffle=True,
    # 										collate_fn=collate_fn,
    # 										worker_init_fn=worker_init_fn
    # 										)

    # Note that due to the way that pytorch and pytorch_lightning works,
    # the two dataloaders need to be seperate and the same for the dataset

    # dataset_val = YOURDATASET(args, train=False)
    # dataloader_val = torch.utls.data.DataLoader(dataset,
    # 											batch_size=args.batch_size,
    # 											shuffle=False,
    # 											collate_fn=collate_fn,
    # 											worker_init_fn=worker_init_fn
    # 											)


    # Setup and load model 

    # model = YOURMODEL(args)

    # NOTE: You can setup mid-training model checkpoints too:
    # https://pytorch-lightning.readthedocs.io/en/latest/common/checkpointing.html

    # NOTE: There is auto learning rate tuning and scheduling in
    # PyTorch Lightning
    # https://pytorch-lightning.readthedocs.io/en/latest/common/trainer.html#auto-lr-find
    # https://pytorch-lightning.readthedocs.io/en/latest/common/optimizers.html?highlight=learning%20rate%20schedule#learning-rate-scheduling

    # Setup trainer

    # Automatic
    # trainer = pl.Trainer.from_argparse_args(args)

    # Manual
    # trainer = pl.Trainer(<YOURARGS>)


    # Log data only when not debugging
    # if args.log:
    #     print("Logging to WandB")
    #     trainer.logger = wandb_logger

    # trainer.fit(model, train_dataloader=dataloader,
    #             val_dataloaders=dataloader_val)


    # Save model after training
    # ckpt_name = "YOURNAMINGMETHOD" + .pth
    # trainer.save_checkpoint(ckpt_name)
    pass