from project.campaigns.base_campaign import BaseCampaign


class LowBudgetCampaign(BaseCampaign):

    def __init__(self, campaign_id: int, brand: str, required_engagement: float, budget=2500.0):
        super().__init__(campaign_id, brand, required_engagement, budget)
