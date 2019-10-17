<template>
    <form class="ui form" @submit.prevent="handleSubmit">
        <div class="content">
            <div class="field" :key="extension[0]" v-for="extension in settings.FILE_EXTENSION_CHOICES">
                <div class="ui radio checkbox">
                    <input :id="extension[0]" v-model="settings.config_file_extension" type="radio" :value="extension[0]">
                    <label :for="extension[0]">{{ extension[1] }}</label>
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
            FILE_EXTENSION_CHOICES: []
        };

        handleSubmit () {
            this.$store.dispatch('setSettings', this.settings);
        }

        mounted () {
            this.settings.config_file_extension = _.cloneDeep(this.$store.state.settings.config_file_extension);
            this.settings.FILE_EXTENSION_CHOICES = _.cloneDeep(this.$store.state.settings.FILE_EXTENSION_CHOICES);
        }

}

</script>

<style scoped lang="scss">

</style>
