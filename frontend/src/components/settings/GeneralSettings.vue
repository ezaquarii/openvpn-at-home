<template>
    <form class="ui form" @submit.prevent="handleSubmit">
        <div class="ui dividing small header">Config File Extension</div>

        <div class="ui small header">Client</div>
        <div class="content">
            <div class="field" :key="extension.value" v-for="extension in settings.client_config_file_extension_choices">
                <div class="ui radio checkbox">
                    <input :id="extension.value" v-model="settings.client_config_file_extension" type="radio" :value="extension.value">
                    <label :for="extension.value">{{ extension.name }}</label>
                </div>
            </div>
        </div>

        <div class="ui small header">Server</div>
        <div class="content">
            <div class="field" :key="extension.value" v-for="extension in settings.server_config_file_extension_choices">
                <div class="ui radio checkbox">
                    <input :id="extension.value" v-model="settings.server_config_file_extension" type="radio" :value="extension.value">
                    <label :for="extension.value">{{ extension.name }}</label>
                </div>
            </div>
            <div class="field">
                <button type="submit" class="ui button settings-button" role="button" @submit="{}">Save</button>
            </div>
        </div>
    </form>
</template>

<script>
import { Component, Vue } from 'vue-property-decorator';
import NavigationBar from '@/components/NavigationBar.vue';
import _ from 'lodash';

@Component({
    name: 'GeneralSettings',
    components: {
        NavigationBar
    }
})
export default class GeneralSettings extends Vue {

        settings = {
            client_config_file_extension: 'conf',
            server_config_file_extension: 'conf',
            client_config_file_extension_choices: [],
            server_config_file_extension_choices: []
        };

        handleSubmit () {
            this.$store.dispatch('setSettings', this.settings);
        }

        mounted () {
            this.settings.client_config_file_extension = _.cloneDeep(this.$store.state.settings.client_config_file_extension);
            this.settings.server_config_file_extension = _.cloneDeep(this.$store.state.settings.server_config_file_extension);
            this.settings.client_config_file_extension_choices = _.cloneDeep(this.$store.state.settings.client_config_file_extension_choices);
            this.settings.server_config_file_extension_choices = _.cloneDeep(this.$store.state.settings.server_config_file_extension_choices);
        }

}

</script>

<style scoped lang="scss">

</style>
