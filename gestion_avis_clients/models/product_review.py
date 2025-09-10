from odoo import api, fields, models, _


class ProductReview(models.Model):
    _name = 'product.review'
    _description = 'Product Review'
    _order = 'review_date desc'
    
    title = fields.Char(string='Title', required=True)
    product_id = fields.Many2one('product.product', string='Product', required=True)
    
    customer_name = fields.Char(string='Customer Name', required=True)
    # customer_id = fields.Many2one('res.partner', string='Customer', domain="[('is_customer', '=', True)]")
    
    rating_stars = fields.Selection([
        ('1', '1 Star'),
        ('2', '2 Stars'),
        ('3', '3 Stars'),
        ('4', '4 Stars'),
        ('5', '5 Stars')
    ], string='Rating', required=True)
    
    rating = fields.Float(string='Rating', compute='_compute_rating_stars', store=True)
    comments = fields.Text(string='Comments', required=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft', required=True)
    
    review_date = fields.Datetime(string='Review Date', default=fields.Datetime.now, required=True)
    
    
    approved_by = fields.Many2one('res.users', string='Approved By')
    
    approved_date = fields.Datetime(string='Approved Date')
    
    
    rejected = fields.Boolean(string='Rejected', default=False)
    rejection_reason = fields.Text(string='Rejection Reason')

    @api.depends('rating_stars')
    def _compute_rating(self):
        for record in self:
            if record.rating_stars:
                record.rating = float(record.rating_stars)
            else:
                record.rating = 0.0
                

    def action_submit_for_approval(self):
        self.write({'state': 'submitted'})
        return True
    
    
    def action_approve(self):
        self.write({
            'state': 'approved',
            'approved_by': self.env.user.id,
            'approved_date': fields.Datetime.now(),
            'rejected': False
            
        })
        return True
    
    def action_reject(self, reason):
        self.write({
            'state': 'rejected',
            'rejected': True,
            # 'rejection_reason': reason
        })
        return True
    

    
