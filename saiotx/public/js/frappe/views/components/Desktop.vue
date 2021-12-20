<template>
	<div class="modules-page-container" v-if="home_settings_fetched">
		<a
			class="btn-show-hide text-muted text-medium"
			@click="show_hide_cards_dialog"
		>
			{{ __('Show / Hide Cards') }}
		</a>
	<div class="row statistics-section">
    <div class="col-md-12">
        <div class="row statistics-container">
			<div class="col-xl-2 col-md-6 col-lg-4" v-for="(card,i) in statistic_cards" :key="card.title">
				<statistic-card :title="card.title" :icon="card.icon" :amount="card.total" ></statistic-card>
			</div>
		</div>
		</div>
	</div>
		
		
		<div
			class="modules-section"
			v-for="(category, i) in module_categories" :key="category"
		>
			<desk-section
				v-if="get_modules_for_category(category).length"
				:category="category"
				:modules="get_modules_for_category(category)"
				@update-desktop-settings="update_desktop_settings"
				@module-order-change="update_module_order"
			>
			</desk-section>
		</div>
	</div>
</template>

<script>
import DeskSection from './DeskSection.vue';
import StatisticCard from './StatisticCard.vue';
import { generate_route } from './utils';

export default {
	components: {
		DeskSection,
		StatisticCard
	},
	data() {
		return {
			module_categories: ['Modules', 'Domains', 'Places', 'Administration'],
			modules: [],
			home_settings_fetched: false,
			statistic_cards : []
		};
	},
	created() {
		this.fetch_desktop_settings();
		this.fetch_statistics_data();
	},
	methods: {
		fetch_desktop_settings() {
			frappe.call('frappe.desk.moduleview.get_desktop_settings')
				.then(r => {
					if (r.message) {
						this.update_desktop_settings(r.message);
						this.home_settings_fetched = true;
					}
				});
		},
		fetch_statistics_data(){
			this.get_daily_purchases();
			this.get_daily_sales();
			this.get_total_sales();
			this.get_total_purchases();
			this.get_statistics_cards();
			this.get_total_purchase_orders();
			this.get_total_sales_orders();

		},
		get_daily_purchases(){
			let title = __("Daily Expenses");
			if(frappe.boot.lang === "ar"){
				title = "المشتريات اليومية"
			}
			frappe.call('saiotx.api.get_daily_purchases')
				.then(r => {
					if (r.message) {
						let card = r.message;
						card.title = title;
						if(!card.total){
							card.total = "0.00"
						}
						card.icon = "fa fa-shopping-cart";
						card.total = frappe.format(card.total,{ fieldtype: 'Currency', options: 'currency' })

						this.statistic_cards.push(card);
					}
				});
		},
		get_total_sales(){
			let title = __("Total Revenue");
			if(frappe.boot.lang === "ar"){
				title = "إجمالي المبيعات"
			}
			frappe.call('saiotx.api.get_total_sales_info')
				.then(r => {
					if (r.message) {
						let card = r.message;
						card.title = title;
						if(!card.total){
							card.total = "0.00"
						}
						card.icon = "fa fa-usd";
						card.total = frappe.format(card.total,{ fieldtype: 'Currency', options: 'currency' })
						this.statistic_cards.push(card);
					}
				});
		},
		get_total_purchases(){
			let title = __("Total Expenses");
			if(frappe.boot.lang === "ar"){
				title = "إجمالي المشتريات"
			}
			frappe.call('saiotx.api.get_total_purchase_info')
				.then(r => {
					if (r.message) {
						let card = r.message;
						card.title = title;
						if(!card.total){
							card.total = "0.00"
						}
						card.total = frappe.format(card.total,{ fieldtype: 'Currency', options: 'currency' })
						card.icon = "fa fa-shopping-cart";
						this.statistic_cards.push(card);
					}
				});
		},
		get_total_purchase_orders(){
			let title = __("Purchase Orders");
			if(frappe.boot.lang === "ar"){
				title = "طلبات الشراء"
			}
			frappe.call('saiotx.api.get_total_purchase_order_info')
				.then(r => {
					if (r.message) {
						let card = r.message;
						card.title = title;
						if(!card.total){
							card.total = "0.00"
						}
						card.icon = "fa fa-shopping-cart";
						card.total = frappe.format(card.total,{ fieldtype: 'Currency', options: 'currency' })

						this.statistic_cards.push(card);
					}
				});
		},
		get_total_sales_orders(){
			let title = __("Sales Orders");
			if(frappe.boot.lang === "ar"){
				title = "طلبات البيع"
			}
			frappe.call('saiotx.api.get_total_sales_order_info')
				.then(r => {
					if (r.message) {
						let card = r.message;
						card.title = title;
						if(!card.total){
							card.total = "0.00"
						}
						card.icon = "fa fa-usd";
						card.total = frappe.format(card.total,{ fieldtype: 'Currency', options: 'currency' })

						this.statistic_cards.push(card);
					}
				});
		},
		get_daily_sales(){
			let title = __("Daily Revenue");
			if(frappe.boot.lang === "ar"){
				title = "المبيعات اليومية"
			}
			frappe.call('saiotx.api.get_daily_sales')
				.then(r => {
					if (r.message) {
						let card = r.message;
						card.title = title;
						if(!card.total){
							card.total = "0.00"
						}
						card.icon = "fa fa-usd";
						card.total = frappe.format(card.total,{ fieldtype: 'Currency', options: 'currency' })

						this.statistic_cards.push(card);
					}
				});
		},
		get_statistics_cards(){
			frappe.call('saiotx.api.get_statistics_cards')
				.then(r => {
					if (r.message) {
						let cards = r.message;
						cards.forEach(card => {
							this.statistic_cards.push(card);
						});
					}
				});
		},
		update_desktop_settings(desktop_settings) {
			this.modules = this.add_routes_for_module_links(desktop_settings);
		},
		add_routes_for_module_links(user_settings) {
			for (let category in user_settings) {
				user_settings[category] = user_settings[category].map(m => {
					m.links = (m.links || []).map(link => {
						link.route = generate_route(link);
						return link;
					});
					return m;
				});
			}
			return user_settings;
		},
		update_module_order({ module_category, modules }) {
			frappe.call('frappe.desk.moduleview.update_modules_order', { module_category, modules });
		},
		get_modules_for_category(category) {
			return this.modules[category] || [];
		},
		show_hide_cards_dialog() {
			frappe.call('frappe.desk.moduleview.get_options_for_show_hide_cards')
				.then(r => {
					let { user_options, global_options } = r.message;

					let user_value = `User (${frappe.session.user})`
					let fields = [
						{
							label: __('Setup For'),
							fieldname: 'setup_for',
							fieldtype: 'Select',
							options: [
								{
									label: __('User ({0})', [frappe.session.user]),
									value: user_value
								},
								{
									label: __('Everyone'),
									value: 'Everyone'
								}
							],
							default: user_value,
							depends_on: doc => frappe.user_roles.includes('System Manager'),
							onchange() {
								let value = d.get_value('setup_for');
								let field = d.get_field('setup_for');
								let description = value === 'Everyone' ? __('Hide cards for all users') : '';
								field.set_description(description);
							}
						}
					];

					let user_section = this.module_categories.map(category => {
						let options = user_options.filter(m => m.category === category);
						return {
							label: category,
							fieldname: `user:${category}`,
							fieldtype: 'MultiCheck',
							options,
							columns: 2
						}
					}).filter(f => f.options.length > 0);

					user_section = [
						{
							fieldname: 'user_section',
							fieldtype: 'Section Break',
							depends_on: doc => doc.setup_for === user_value
						}
					].concat(user_section);

					let global_section = this.module_categories.map(category => {
						let options = global_options.filter(m => m.category === category);
						return {
							label: category,
							fieldname: `global:${category}`,
							fieldtype: 'MultiCheck',
							options,
							columns: 2
						}
					}).filter(f => f.options.length > 0);

					global_section = [
						{
							fieldname: 'global_section',
							fieldtype: 'Section Break',
							depends_on: doc => doc.setup_for === 'Everyone'
						}
					].concat(global_section);

					fields = fields.concat(user_section, global_section);

					let old_values = null;
					const d = new frappe.ui.Dialog({
						title: __('Show / Hide Cards'),
						fields: fields,
						primary_action_label: __('Save'),
						primary_action: (values) => {
							if (values.setup_for === 'Everyone') {
								this.update_global_modules(d);
							} else {
								this.update_user_modules(d, old_values);
							}
						}
					});

					d.show();

					// deepcopy
					old_values = JSON.parse(JSON.stringify(d.get_values()));
				});
		},

		update_user_modules(d, old_values) {
			let new_values = d.get_values();
			let category_map = {};
			for (let category of this.module_categories) {
				let old_modules = old_values[`user:${category}`] || [];
				let new_modules = new_values[`user:${category}`] || [];

				let removed = old_modules.filter(module => !new_modules.includes(module));
				let added = new_modules.filter(module => !old_modules.includes(module));

				category_map[category] = { added, removed };
			}

			frappe.call({
				method: 'frappe.desk.moduleview.update_hidden_modules',
				args: { category_map },
				btn: d.get_primary_btn()
			}).then(r => {
				this.update_desktop_settings(r.message);
				d.hide();
			});
		},

		update_global_modules(d) {
			let blocked_modules = [];
			for (let category of this.module_categories) {
				let field = d.get_field(`global:${category}`);
				if (field) {
					let unchecked_options = field.get_unchecked_options();
					blocked_modules = blocked_modules.concat(unchecked_options);
				}
			}

			frappe.call({
				method: 'frappe.desk.moduleview.update_global_hidden_modules',
				args: {
					modules: blocked_modules
				},
				btn: d.get_primary_btn()
			}).then(r => {
				this.update_desktop_settings(r.message);
				d.hide();
			});
		}
	}
}
</script>

<style lang="less" scoped>
.modules-page-container {
	position: relative;
	margin-top: 40px;
	margin-bottom: 30px;
	padding-top: 1px;
}

.modules-section {
	position: relative;
	margin-top: 30px;
}

.btn-show-hide {
	position: absolute;
	right: 0;
	top: 39px;
	z-index: 1;
}
.frappe-rtl .btn-show-hide{
	right: unset;
	left: 0;
}

.toolbar-underlay {
	margin: 70px;
}

.btn-show-hide{
	padding: 10px;
	margin: -28px;
	border: solid 1px aliceblue;
	background-color: aliceblue;
	border-radius: 10px;

}
.btn-show-hide:hover{
	background-color: #48c1c9;
	color: white!important;
}

</style>

