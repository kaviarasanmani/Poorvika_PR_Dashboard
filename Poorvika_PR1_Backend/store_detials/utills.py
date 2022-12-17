from .models import Edition, Store, Publication,EditionSave


class EditionData:

    def __init__(self, ed_dis_value=None, ed_dis_count=None, dis_play=None):
        # self.ed_dis_value = ed_dis_value
        self.ed_dis_count = ed_dis_count
        # self.dis_play = dis_play

    def edition_loc(self, **kwargs):
        edition_loc_list = []
        print("#"*150)

        for Ed in Edition.objects.filter(Edition=kwargs.get('edition_location'),
                                         Pub_id=Publication.objects.get(name=kwargs.get('edition'))):
            edition_loc_list.append(Ed.District)

        self.edition_store(Store_District=edition_loc_list, Store_Value=kwargs.get('edition_value'),
                           Store_Edition=kwargs.get('edition'), store_location=kwargs.get('edition_location'))

    def edition_store(self, **kwargs):
        all_store = {}
        data_count = int()
        store_list =[]
        location_and_count = {}

        all_store["Edition"] = kwargs.get('Store_Edition'),
        all_store["Location"] = kwargs.get('store_location'),
        all_store["Get Location"] = kwargs.get('Store_District'),


        for store in kwargs.get('Store_District'):
            data_count += Store.objects.filter(DISTRICT=store, STATUS='ACTIVE').count()
            location_and_count[store] = Store.objects.filter(DISTRICT=store, STATUS='ACTIVE').count()


        for store in kwargs.get('Store_District'):
            store_active_count = Store.objects.filter(DISTRICT=store, STATUS='ACTIVE').count()
            store_count = Store.objects.filter(DISTRICT=store).count()

            for store_id in Store.objects.filter(DISTRICT=store, STATUS='ACTIVE'):

                # store_list.append(store_id.SHORT_CODE)

                store_list.append(store_id.SHOWROOM.location)
            all_store["SHOWROOM"] = store_list
            all_store[store] = "All Store", store_count, "Active Store", store_active_count
        all_store['Store Count'] = location_and_count
        all_store["All Active Store"] = data_count
        all_store["Total Average"] = round(kwargs.get('Store_Value') / data_count)

        self.ed_dis_count = dict(all_store)

    def edition_display(self):
        return self.ed_dis_count
