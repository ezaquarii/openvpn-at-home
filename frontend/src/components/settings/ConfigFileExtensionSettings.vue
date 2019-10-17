<template>
    <form class="ui form" @submit.prevent="handleSubmit">
        <div class="content">
            <div class="field" :key="extension.value" v-for="extension in settings.config_file_extension_choices">
                <div class="ui radio checkbox">
                    <input :id="extension.value" v-model="settings.config_file_extension" type="radio" :value="extension.value">
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
    name: 'ConfigFileExtensionSettings',
    components: {
        NavigationBar
    }
})
export default class ConfigFileExtensionSettings extends Vue {

        settings = {
            config_file_extension: 'conf',
            config_file_extension_choices: []
        };

        handleSubmit () {
            this.$store.dispatch('setSettings', this.settings);
        }

        mounted () {
            this.settings.config_file_extension = _.cloneDeep(this.$store.state.settings.config_file_extension);
            this.settings.config_file_extension_choices = _.cloneDeep(this.$store.state.settings.config_file_extension_choices);
        }

}

</script>

<style scoped lang="scss">

</style>
